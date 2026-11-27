// Checks a parsed label file v2 (admin/model-labels/labels.yaml) and returns its problems as
// "<rel>: <entry>: <problem>" messages. Used by validate.mjs; self-test: model-labels.test.mjs.
//
//   version: 2
//   locales: [de, en]
//   groups:  [{ id, label, icon? }]
//   models:  [{ model, group, menu?, supersededBy?, aliases?, endpoints?, label, description? }]
//
// Unknown keys are rejected everywhere (strict). The rules mirror the tenant-side reader in companyADMIN
// (src/services/label-file.ts, `validate`), so a file that passes here is accepted by every tenant. The one intended
// difference: descriptions are one line of at most 120 characters here (README rule), the reader allows 512.

const TOP_KEYS = ['version', 'locales', 'groups', 'models'];
const GROUP_KEYS = ['id', 'label', 'icon'];
const MODEL_KEYS = ['model', 'group', 'menu', 'supersededBy', 'aliases', 'endpoints', 'label', 'description'];
const MENU = ['featured', 'available'];
const LOCALE_RE = /^[a-z]{2}(-[A-Z]{2})?$/;
const LABEL_MAX = 128; // also the limit for model ids
const ICON_MAX = 512;
const PROVIDER_ICON_RE = /^[A-Za-z][A-Za-z0-9_.-]{0,127}$/;
const HTTPS_ICON_RE = /^https:\/\/[^\s]+$/;
/** The reader rejects larger files before parsing; validate.mjs applies it to the raw text. */
export const MAX_FILE_CHARS = 1_000_000;
const DESCRIPTION_MAX = 120; // README rule (one line); the format itself would allow 512
// eslint-disable-next-line no-control-regex
const CONTROL_RE = /[\u0000-\u001f\u007f-\u009f]/;

const isObject = (v) => typeof v === 'object' && v !== null && !Array.isArray(v);

export function validateModelLabels(doc, rel) {
	const errors = [];
	const fail = (where, msg) => errors.push(`${rel}: ${where ? `${where}: ` : ''}${msg}`);
	const strict = (where, obj, allowed) => {
		for (const key of Object.keys(obj)) if (!allowed.includes(key)) fail(where, `unknown key "${key}"`);
	};

	if (!isObject(doc)) {
		fail('', 'must be a mapping with version: 2');
		return errors;
	}
	strict('', doc, TOP_KEYS);
	if (doc.version !== 2) fail('', `version must be 2 (is ${JSON.stringify(doc.version)})`);

	// Like the reader: a list with any non-string entry counts as no locales at all.
	const locales = Array.isArray(doc.locales) && doc.locales.every((L) => typeof L === 'string') ? doc.locales : [];
	if (!locales.length || locales.some((L) => !LOCALE_RE.test(L)) || new Set(locales).size !== locales.length) {
		fail('', `locales must be a non-empty list of unique locale codes such as [de, en] (is ${JSON.stringify(doc.locales)})`);
	}

	// One text value: labels 1–128 characters without control characters, descriptions at most 120 characters.
	const text = (where, name, value, field) => {
		if (value === undefined || value === null) return fail(where, `${name} is missing`);
		if (typeof value !== 'string') return fail(where, `${name} must be a string`);
		if (field === 'label') {
			if (!value.trim()) fail(where, `${name} is empty`);
			if (value.length > LABEL_MAX) fail(where, `${name} is longer than ${LABEL_MAX} characters`);
			if (CONTROL_RE.test(value)) fail(where, `${name} contains control characters`);
		} else if (value.length > DESCRIPTION_MAX) {
			fail(where, `${name} is longer than ${DESCRIPTION_MAX} characters`);
		}
	};
	// A translated text: a { <locale>: string } map carrying exactly the listed locales.
	const texts = (where, field, value) => {
		if (!isObject(value)) return fail(`${where}: ${field}`, `must be a map with ${locales.join(', ')}`);
		strict(`${where}: ${field}`, value, locales);
		for (const L of locales) text(where, `${field}.${L}`, value[L], field);
	};

	const groupIds = new Set();
	if (!Array.isArray(doc.groups)) fail('', 'groups must be a list');
	const groups = Array.isArray(doc.groups) ? doc.groups : [];
	for (const [i, g] of groups.entries()) {
		const where = `groups[${isObject(g) && typeof g.id === 'string' && g.id ? g.id : i}]`;
		if (!isObject(g)) {
			fail(where, 'must be a mapping');
			continue;
		}
		strict(where, g, GROUP_KEYS);
		if (typeof g.id !== 'string' || !g.id) fail(where, 'id must be a non-empty string');
		else if (groupIds.has(g.id)) fail(where, `id "${g.id}" is used twice`);
		else groupIds.add(g.id);
		if (typeof g.label === 'string') text(where, 'label', g.label, 'label');
		else if (g.label === undefined) fail(where, 'label is required (a string or a map with every locale)');
		else texts(where, 'label', g.label);
		if (
			g.icon !== undefined &&
			!(typeof g.icon === 'string' && g.icon.length <= ICON_MAX && (PROVIDER_ICON_RE.test(g.icon) || HTTPS_ICON_RE.test(g.icon)))
		) {
			fail(where, `icon must be a provider icon name or an https:// URL of at most ${ICON_MAX} characters`);
		}
	}

	// Optional list of non-empty strings.
	const list = (where, key, value) => {
		if (value === undefined) return [];
		if (!Array.isArray(value) || value.some((v) => typeof v !== 'string' || !v)) {
			fail(where, `${key} must be a list of non-empty strings`);
			return [];
		}
		return value;
	};

	const ids = new Set(); // model ids and aliases share one namespace
	const claim = (where, id) => {
		if (ids.has(id)) fail(where, `id "${id}" is used twice (model ids and aliases must be unique)`);
		ids.add(id);
	};

	if (!Array.isArray(doc.models)) fail('', 'models must be a list');
	const models = Array.isArray(doc.models) ? doc.models : [];
	const successors = new Map(); // model id -> supersededBy (as written)
	for (const [i, m] of models.entries()) {
		const where = isObject(m) && typeof m.model === 'string' && m.model ? m.model : `models[${i}]`;
		if (!isObject(m)) {
			fail(where, 'must be a mapping');
			continue;
		}
		strict(where, m, MODEL_KEYS);
		if (typeof m.model !== 'string' || !m.model) fail(where, 'model must be a non-empty string');
		else if (m.model.length > LABEL_MAX || CONTROL_RE.test(m.model)) {
			fail(where, `model must have at most ${LABEL_MAX} characters without control characters`);
		} else claim(where, m.model);
		for (const alias of list(where, 'aliases', m.aliases)) claim(where, alias);
		const endpoints = list(where, 'endpoints', m.endpoints);
		for (const [j, e] of endpoints.entries()) if (endpoints.indexOf(e) !== j) fail(where, `endpoints lists "${e}" twice`);
		const next = list(where, 'supersededBy', m.supersededBy);
		if (typeof m.model === 'string' && m.model && !successors.has(m.model)) successors.set(m.model, next);
		if (!groupIds.has(m.group)) fail(where, `unknown group "${m.group ?? ''}"`);
		if (m.menu !== undefined && !MENU.includes(m.menu)) fail(where, `menu must be ${MENU.join(' or ')} (is ${JSON.stringify(m.menu)})`);
		texts(where, 'label', m.label);
		if (m.description !== undefined) texts(where, 'description', m.description);
	}

	// Successors are canonical model ids of this file, and following them never leads back.
	for (const [id, next] of successors) {
		for (const s of next) if (!successors.has(s)) fail(id, `supersededBy: unknown model "${s}" (must be a model id of this file)`);
	}
	const state = new Map(); // id -> 'open' while on the DFS path, 'done' afterwards
	const visit = (id, path) => {
		if (state.get(id) === 'done') return;
		if (state.get(id) === 'open') {
			const cycle = [...path.slice(path.indexOf(id)), id];
			fail(cycle[0], `supersededBy has a cycle: ${cycle.join(' -> ')}`);
			return;
		}
		state.set(id, 'open');
		for (const s of successors.get(id) ?? []) if (successors.has(s)) visit(s, [...path, id]);
		state.set(id, 'done');
	};
	for (const id of successors.keys()) visit(id, []);

	return errors;
}
