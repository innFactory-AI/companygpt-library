---
name: de-tool-search
description: Verwende diesen Skill immer dann, wenn du ein Tool für eine bestimmte Aufgabe finden, auswählen und ausführen musst, dessen exakten Namen und Eingabeschema du noch nicht kennst.
---

# Tool-Suche Skill

Findet über die Tool-Suche das passende Tool, wählt es anhand von Name und Schema aus und führt es anschließend mit den richtigen Parametern aus.

## Schritt 1: Verfügbare Tools ermitteln

Rufe zuerst das Tool `search_tools` (bzw. `tool_search`) auf, um herauszufinden, welche Tools überhaupt existieren.

- **Die Query-Regel:** Der Parameter `query` MUSS ein generischer, funktionaler Suchbegriff sein, der beschreibt, *was* du erreichen willst (z. B. `"search"`, `"files"`, `"excel"`, `"database"`, `"sql"`, `"image"`).
- **KRITISCH – Verwende NICHT die inhaltliche Suchanfrage des Benutzers.** Suche also nicht nach `"maschinelles Lernen"` oder `"machine learning"`.
- **KRITISCH – Übergib KEINE tool-spezifischen Argumente** (wie `collection`, `topK`, `searchMode`, `mcp_server`) an die Tool-Suche. Nutze ausschließlich die Argumente, die im Schema des Such-Tools definiert sind.

Beispielaufruf:

```json
{
  "query": "search"
}
```

## Schritt 2: Das richtige Tool analysieren und auswählen

Prüfe die Liste der Tools, die die Suche zurückgegeben hat.

1. **Exakten Namen übernehmen:** Sieh dir das Feld `name` des passenden Tools an. Du musst den vollständigen, exakten Namen verwenden (z. B. `search_content_mcp_ai-search`, NIEMALS verkürzt zu `search_content`).
2. **Schema lesen:** Lies die Beschreibung und die Parameterdefinitionen des Tools, um zu verstehen, welche Parameter erwartet werden.

## Schritt 3: Das ausgewählte Tool ausführen

Rufe das ausgewählte Tool auf.

- Erst in diesem Schritt setzt du die tatsächliche Suchanfrage des Benutzers, Filter und operative Parameter ein (z. B. `collection: "ai_rag_ml"`, `searchMode`, `query`).
- Halte dich exakt an das Eingabeschema des Ziel-Tools. Übernimm keine Parameter aus dem Suchschritt.

## Grundregeln

| Regel | Bedeutung |
| --- | --- |
| **Strikte Parametertrennung** | Mische niemals Parameter der Tool-Suche (Discovery-Query) mit operativen Parametern (`collection`, `topK`, …). |
| **Query-Unterscheidung** | Funktionaler Tool-Suchbegriff (z. B. `"search"`) ≠ inhaltliche Benutzeranfrage (z. B. `"maschinelles Lernen"`). |
| **Exakter Name** | Kopiere den vollständigen Tool-Namen zeichengenau, um „Tool not found"-Fehler zu vermeiden. |
