#!/usr/bin/env node
// Checks the repo layout before the docs build or companyADMIN Library Sync ever sees it.
//
//   skills/<category>/<locale>-<id>/SKILL.md   name == folder, locale prefix, both locales, listed under <category>
//   pages/<category>/<id>.<locale>.md          one docs wrapper per catalog entry and locale
//   agents/<locale>-<slug>.yaml                unique ids, skills/subagents resolve within the same locale
//   admin/model-labels/<locale>.yaml           same model list in every locale
//
// Usage: npm run validate
import { existsSync, readFileSync, readdirSync } from 'node:fs';
import { join, resolve } from 'node:path';
import { parse } from 'yaml';

const LOCALES = ['de', 'en'];
const NAME_RE = /^[a-z0-9][a-z0-9-]*$/;
const root = resolve(process.argv[2] || '.');
const errors = [];
const fail = (msg) => errors.push(msg);
const read = (rel) => readFileSync(join(root, rel), 'utf8');
const dirs = (rel) =>
	existsSync(join(root, rel)) ? readdirSync(join(root, rel), { withFileTypes: true }).filter((d) => d.isDirectory()).map((d) => d.name) : [];

function frontmatter(rel) {
	const m = read(rel).match(/^---\n([\s\S]*?)\n---\n?/);
	if (!m) {
		fail(`${rel}: missing YAML frontmatter`);
		return {};
	}
	try {
		return parse(m[1]) || {};
	} catch (e) {
		fail(`${rel}: frontmatter is not valid YAML (${e.message.split('\n')[0]})`);
		return {};
	}
}

// catalog.json
const catalog = JSON.parse(read('catalog.json'));
const listed = new Map(); // id -> category
for (const cat of catalog.categories) {
	for (const L of LOCALES) if (!cat.label?.[L]) fail(`catalog.json: category ${cat.id} needs label.${L}`);
	for (const id of cat.skills) {
		if (listed.has(id)) fail(`catalog.json: ${id} is listed twice`);
		listed.set(id, cat.id);
	}
}
for (const L of LOCALES) {
	for (const key of ['title', 'description', 'intro']) if (!catalog.index?.[L]?.[key]) fail(`catalog.json: index.${L}.${key} missing`);
}

// skills/<category>/
const skillNames = new Set();
const categories = new Set(catalog.categories.map((c) => c.id));
for (const cat of dirs('skills')) {
	if (!categories.has(cat)) fail(`skills/${cat}: not a category in catalog.json`);
	for (const folder of dirs(`skills/${cat}`)) {
		const rel = `skills/${cat}/${folder}/SKILL.md`;
		const m = folder.match(/^([a-z]{2})-(.+)$/);
		if (!m || !LOCALES.includes(m[1])) {
			fail(`skills/${cat}/${folder}: folder must be <${LOCALES.join('|')}>-<id>`);
			continue;
		}
		if (!existsSync(join(root, rel))) {
			fail(`${rel}: missing`);
			continue;
		}
		const [, L, id] = m;
		const fm = frontmatter(rel);
		if (fm.name !== folder) fail(`${rel}: name must be "${folder}" (is "${fm.name}")`);
		if (!NAME_RE.test(folder) || folder.length > 64) fail(`${rel}: name must match ${NAME_RE} and have at most 64 characters`);
		if (!fm.description) fail(`${rel}: frontmatter needs description`);
		else if (String(fm.description).length > 1024) fail(`${rel}: description longer than 1024 characters`);
		if (read(rel).length > 100_000) fail(`${rel}: longer than 100,000 characters`);
		if (listed.get(id) !== cat) fail(`skills/${cat}/${folder}: ${id} is not listed under ${cat} in catalog.json`);
		if (skillNames.has(folder)) fail(`skills/${cat}/${folder}: name ${folder} exists twice`);
		skillNames.add(folder);
	}
}
for (const [id, cat] of listed) {
	for (const L of LOCALES) {
		if (!existsSync(join(root, 'skills', cat, `${L}-${id}`, 'SKILL.md'))) fail(`skills/${cat}/${L}-${id}/SKILL.md: missing (listed in catalog.json)`);
		const page = `pages/${cat}/${id}.${L}.md`;
		if (!existsSync(join(root, page))) {
			fail(`${page}: missing`);
			continue;
		}
		const fm = frontmatter(page);
		for (const key of ['title', 'description', 'label']) if (!fm[key]) fail(`${page}: frontmatter needs ${key}`);
	}
}
for (const cat of dirs('pages')) {
	for (const f of readdirSync(join(root, 'pages', cat)).filter((n) => n.endsWith('.md'))) {
		const m = f.match(/^(.+)\.([a-z]{2})\.md$/);
		if (!m || !LOCALES.includes(m[2])) fail(`pages/${cat}/${f}: file must be <id>.<${LOCALES.join('|')}>.md`);
		else if (listed.get(m[1]) !== cat) fail(`pages/${cat}/${f}: not listed under ${cat} in catalog.json`);
	}
}

// agents/
const agents = [];
for (const f of existsSync(join(root, 'agents')) ? readdirSync(join(root, 'agents')) : []) {
	if (!/\.ya?ml$/.test(f)) continue;
	const rel = `agents/${f}`;
	const L = f.slice(0, 2);
	if (!LOCALES.includes(L) || f[2] !== '-') fail(`${rel}: file name must start with <${LOCALES.join('|')}>-`);
	let a;
	try {
		a = parse(read(rel));
	} catch (e) {
		fail(`${rel}: not valid YAML (${e.message.split('\n')[0]})`);
		continue;
	}
	if (!a?.id || !a?.name) fail(`${rel}: needs id and name`);
	else if (!a.id.startsWith(`agent_${L}_`)) fail(`${rel}: id must start with agent_${L}_`);
	agents.push({ rel, L, a });
}
const agentIds = new Map();
for (const { rel, a } of agents) {
	if (agentIds.has(a.id)) fail(`${rel}: id ${a.id} also used by ${agentIds.get(a.id)}`);
	agentIds.set(a.id, rel);
}
for (const { rel, L, a } of agents) {
	for (const s of a.skills || []) {
		if (!skillNames.has(s)) fail(`${rel}: skill "${s}" does not exist`);
		else if (!s.startsWith(`${L}-`)) fail(`${rel}: skill "${s}" is not a ${L} skill`);
	}
	for (const id of a.subagents?.agent_ids || []) {
		if (!agentIds.has(id)) fail(`${rel}: subagent ${id} does not exist`);
		else if (!id.startsWith(`agent_${L}_`)) fail(`${rel}: subagent ${id} is not a ${L} agent`);
	}
}

// admin/model-labels/
const labelModels = {};
for (const L of LOCALES) {
	const rel = `admin/model-labels/${L}.yaml`;
	if (!existsSync(join(root, rel))) {
		fail(`${rel}: missing`);
		continue;
	}
	let doc;
	try {
		doc = parse(read(rel));
	} catch (e) {
		fail(`${rel}: not valid YAML (${e.message.split('\n')[0]})`);
		continue;
	}
	const list = doc?.modelSpecs?.list;
	if (!Array.isArray(list)) {
		fail(`${rel}: needs modelSpecs.list`);
		continue;
	}
	const names = new Set();
	for (const s of list) {
		if (!s.name || !s.label || !s.preset?.endpoint || !s.preset?.model) fail(`${rel}: ${s.name || '?'} needs name, label, preset.endpoint and preset.model`);
		if (names.has(s.name)) fail(`${rel}: ${s.name} is listed twice`);
		names.add(s.name);
	}
	if (list.filter((s) => s.default).length > 1) fail(`${rel}: more than one default`);
	labelModels[L] = list.map((s) => `${s.name}=${s.preset?.endpoint}/${s.preset?.model}`).join(',');
}
if (labelModels.de && labelModels.en && labelModels.de !== labelModels.en) fail('admin/model-labels: de.yaml and en.yaml must list the same models in the same order');

if (errors.length) {
	console.error(`validate: ${errors.length} problem(s):\n  - ${errors.join('\n  - ')}`);
	process.exit(1);
}
console.log(`validate: ${skillNames.size} skills, ${agents.length} agents, ${LOCALES.length} model label lists OK`);
