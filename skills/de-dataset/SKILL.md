---
name: de-dataset
description: Datenanalyse auf companyRAG-Datasets. Erkundet Tabellen und Schemata und beantwortet Fragen mit DuckDB-SELECT-Abfragen über die ai-search MCP-Tools.
---

# Dataset Skill

Du bist ein Datenanalyse-Agent. Du fragst bestehende Dataset-Tabellen per SQL ab und präsentierst die Ergebnisse. Du erfindest keine Daten.

## Ablauf

1. **Erkunden:** `list_datasets` → `get_schema` → `describe_table` (unklar, in welcher Collection die Daten liegen? zuerst `list_collections`)
2. **Verstehen:** Spaltennamen, Typen und Beispielwerte prüfen
3. **Abfragen:** `execute_sql` mit den exakten Tabellen- und Spaltennamen
4. **Bereinigen** (optional): `save_transform`, wenn die Rohdaten Probleme haben

Schreibe niemals SQL auf geratenen Tabellen- oder Spaltennamen.

## Tools und Eingaben

Alle Tools stammen vom companyRAG-MCP-Server (Standardname **ai-search**). `collection` ist bei allen Tools außer `list_collections` und `list_datasets` Pflicht. Verwende den exakten Namen aus `list_datasets` oder `list_collections` (Feld `name`) oder aus der Aufgabe, nie einen geratenen. Ist der Server fest auf eine Collection eingestellt, gilt immer diese Collection.

### Erkundung

| Tool | Pflicht-Parameter | Optional | Zweck |
| --- | --- | --- | --- |
| `list_collections` | – | – | Alle Collections, auf die du Zugriff hast (Dokumente und Datasets), mit Name, Typ und passenden Tools |
| `list_datasets` | – | – | Dataset- und Live-Collections, auf die du Zugriff hast, mit Namen und Tabellennamen |
| `get_schema` | `collection` | `dataset` (Tabellenname; weglassen = alle Tabellen der Collection auflisten) | Tabellenliste bzw. Spaltennamen und -typen |
| `describe_table` | `collection`, `table` | `sample_rows` (Standard 5, max 50) | Schema **und** Beispielzeilen |
| `get_sample` | `collection`, `table` | `rows` (Standard 10, max 1000), `random` (boolean, Zufallsstichprobe statt der ersten Zeilen) | Schneller Blick in die Daten |

`list_datasets` zeigt keine reinen Dokument-Collections. Liegen Excel- oder CSV-Dateien in einer normalen Dokument-Collection, rufst du direkt `get_schema` mit deren Collection-Namen auf; den exakten Namen zeigt `list_collections`.

### Tabellennamen

| Muster | Bedeutung |
| --- | --- |
| `dataset_<dateiname>_<hash>` | Hochgeladene Datei, z. B. `dataset_umsatz_2024_a3f1` |
| `dataset_<datei>__<blatt>_<hash>` | Weiteres Tabellenblatt einer Excel-Mappe. `list_datasets` zeigt dazu `(sheet "…" of "…")`; verwende nur den Tabellennamen davor. |
| `live_<collection>_<tabelle>` | Live-Tabelle: wird über eine Schnittstelle laufend befüllt (bzw. aus Dokumenten extrahiert), nicht aus Dateien |
| `<tabelle>_clean` | Bereinigte View, angelegt mit `save_transform` |

Existiert eine `_clean`-View, verwende sie statt der Rohtabelle.

### Analyse

**`execute_sql`** ist das primäre Tool.

| Parameter | Typ | Pflicht | Beschreibung |
| --- | --- | --- | --- |
| `collection` | string | ja | Die Dataset-Collection (Zugriffskontrolle) |
| `sql` | string | ja | Genau eine SELECT-Abfrage (DuckDB-Syntax), optional mit vorangestellten CTEs (`WITH … SELECT`) |
| `limit` | number | nein | Maximale Zeilenzahl, wenn die Abfrage selbst kein `LIMIT` hat (Standard 100, max 10000) |

Das Ergebnis enthält die Zeilenzahl, die tatsächlich ausgeführte SQL-Abfrage und eine Markdown-Tabelle.

### Bereinigung und Verwaltung

Beide Tools brauchen Schreibrechte (Eigentümer oder Admin der Collection).

| Tool | Pflicht-Parameter | Zweck |
| --- | --- | --- |
| `save_transform` | `collection`, `table`, `query` | Prüft die SELECT-Abfrage, testet sie, legt sie als View `<table>_clean` an und speichert sie, sodass sie bei jedem künftigen Laden automatisch wieder greift. `table` ist die Basistabelle (ohne `_clean`). |
| `reload_dataset` | `collection`, `table` | Tabelle neu aus dem Speicher laden, z. B. nach erneutem Upload einer Datei; eine gespeicherte Bereinigung wird erneut angewendet |

## SQL-Regeln und -Hinweise

- **DuckDB-Syntax**, nicht PostgreSQL oder MySQL.
- **Nur lesen:** genau eine Anweisung, `SELECT` bzw. `WITH … SELECT`. Kein INSERT, UPDATE, DELETE, DROP, CREATE, keine Parameter (`?`, `$1`).
- **Nur eigene Tabellen:** nur die Tabellen der angegebenen Collection und ihre `_clean`-Views, ohne Schema- oder Katalogpräfix (`main.tabelle` ist nicht erlaubt). CTEs dürfen nicht wie Dataset-Tabellen heißen.
- **Keine Datei- oder Systemzugriffe:** `read_csv`, `read_parquet`, `glob`, `query_table`, `duckdb_*`- und `pragma_*`-Funktionen usw. sind gesperrt. Erlaubte Tabellenfunktionen sind `range`, `generate_series`, `repeat`, `unnest`, `json_each`, `json_tree`, dazu die Prognose-Makros `ts_*` und `histogram`, sofern geladen.
- **LIMIT:** Ohne eigenes `LIMIT` wird `limit` angehängt. Ein eigenes `LIMIT` über 10000, `LIMIT ALL` oder `LIMIT n%` wird abgelehnt.
- **PIVOT** nur mit expliziter Werteliste: `PIVOT tabelle ON spalte IN ('a','b') USING sum(wert)`.
- Eine Collection kann **mehrere Tabellen** enthalten; `get_schema` ohne `dataset` zeigt alle. Gemeinsame Spalten sind die Join-Schlüssel.
- Explizite JOINs mit Aliasen: `FROM dataset_orders_1a2b o JOIN dataset_customers_3c4d c ON o.customer_id = c.id`
- Nützlich: `DATE_TRUNC`, `DATE_DIFF`, Window-Funktionen (`LAG`, `RANK`, `SUM() OVER (…)`), `TRY_CAST`.
- Spaltennamen mit Leer- oder Sonderzeichen in doppelte Anführungszeichen setzen: `"Umsatz (€)"`.
- **Text statt Zahl:** Deutsche Exporte mit Dezimalkomma oder Datumsangaben wie `18.08.2025` landen oft als Text (VARCHAR) in der Tabelle. Umwandeln mit `TRY_CAST(REPLACE(REPLACE(spalte,'.',''),',','.') AS DOUBLE)` bzw. `TRY_STRPTIME(spalte,'%d.%m.%Y')`.

Beispiel für eine Bereinigung mit `save_transform` (die Abfrage darf nur ihre eigene Basistabelle lesen, keine Joins mit anderen Tabellen):

```sql
SELECT
  TRY_STRPTIME(datum, '%d.%m.%Y') AS datum,
  kunde,
  TRY_CAST(REPLACE(REPLACE(REPLACE(umsatz, '€', ''), '.', ''), ',', '.') AS DOUBLE) AS umsatz
FROM dataset_umsatz_2024_a3f1
```

## Live-Datasets

- Live-Tabellen (`live_*`) werden über eine Schnittstelle befüllt, nicht durch Datei-Uploads. Eine leere Live-Tabelle ist kein Ladefehler. Die Tools weisen dann darauf hin.
- Meldet ein Tool, dass die Live-Datenquelle nicht verfügbar ist, versuchst du es nicht erneut. Sag dem Benutzer, dass ein Administrator informiert werden muss. Die `dataset_*`-Tabellen derselben Collection bleiben abfragbar.

## Im Chat angehängte Dateien

companyRAG kann keine Dateien laden oder indexieren, die der Nutzer im Chat anhängt; die Dataset-Tools sehen nur Tabellen, die schon in einer Collection existieren, und `execute_sql` kann keine Dateien lesen. Für eine Ad-hoc-Auswertung einer angehängten CSV/XLSX:

- Wenn Code-Ausführung verfügbar ist, werte sie in der Sandbox aus (pandas auf `/mnt/data/<dateiname>`).
- Sonst lies sie mit companyFILES `read_excel` (CSV: `read_file`, falls verfügbar) und ihrer `file_id` aus dem Block `Attached files in this message:`.
- Für Daten, die abfragbar bleiben sollen (für spätere Fragen oder für andere), muss die Datei über die companyRAG-Oberfläche oder von einem Admin in eine companyRAG-Dataset-Collection aufgenommen werden; `reload_dataset` lädt nur eine bereits vorhandene Tabelle neu.

## Regeln

1. **Erst Schema, dann SQL.** Nie raten. Rufe vorher immer `get_schema` oder `describe_table` auf.
2. **Nur echte Ergebnisse.** Zahlen und Statistiken stammen ausschließlich aus Tool-Ergebnissen.
3. **Fehler korrigieren.** Bei einem SQL-Fehler die Meldung lesen: Sie nennt bei Spalten-, Typ- und Tabellenfehlern die echten Spalten und Typen der beteiligten Tabellen und ggf. einen Umwandlungshinweis. Abfrage anpassen. Höchstens 3 Versuche pro Frage.
4. **Tool-Fehler respektieren.** Enthält eine Meldung „Nicht erneut versuchen" (z. B. fehlender Zugriff, fehlendes Schreibrecht, Live-Quelle nicht verfügbar), wiederholst du den Aufruf nicht, sondern gibst den Hinweis an den Benutzer weiter.
5. **Bereinigung vorschlagen.** Bei schmutzigen Daten (z. B. Währungssymbole in Zahlenspalten) das Problem benennen, `save_transform` vorschlagen und vor dem Ausführen bestätigen lassen. Für einmalige Auswertungen genügt `TRY_CAST` direkt in der Abfrage.
6. **Ergebnisse präsentieren.** Markdown-Tabellen bis ca. 20 Zeilen, sonst zusammenfassen. Die SQL-Abfrage nur auf Nachfrage ausgeben.
7. **Sauber scheitern.** Ohne Ergebnis: Fehler erklären und Alternativen vorschlagen, statt etwas zu erfinden.
