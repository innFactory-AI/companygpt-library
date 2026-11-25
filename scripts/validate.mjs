#!/usr/bin/env node
// Checks the repo layout before the docs build or companyADMIN Library Sync ever sees it.
//
//   skills/<category>/<locale>-<id>/SKILL.md   name == folder, locale prefix, both locales, listed under <category>
//   agents/<locale>-<slug>.md                  agent markdown: id agent_<locale>_<slug>, skills/subagents within the locale
//   admin/model-labels/labels.yaml             label file v2 (scripts/model-labels.mjs)
//
// Usage: npm run validate
import { existsSync, readFileSync, readdirSync } from 'node:fs';
import { join, resolve } from 'node:path';
import { parse } from 'yaml';
import { validateModelLabels } from './model-labels.mjs';

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
	}
}

// agents/ (agent markdown, companyADMIN 3.20.0: every agent field in the frontmatter, the instructions as the body)
const agents = [];
for (const f of existsSync(join(root, 'agents')) ? readdirSync(join(root, 'agents')) : []) {
	const rel = `agents/${f}`;
	if (/\.ya?ml$/.test(f)) {
		fail(`${rel}: agents are agent markdown now (agents/<locale>-<slug>.md)`);
		continue;
	}
	if (!f.endsWith('.md') || f === 'README.md') continue;
	const m = f.match(/^([a-z]{2})-([a-z0-9][a-z0-9-]*)\.md$/);
	if (!m || !LOCALES.includes(m[1])) {
		fail(`${rel}: file name must be <${LOCALES.join('|')}>-<slug>.md`);
		continue;
	}
	const [, L, slug] = m;
	const a = frontmatter(rel);
	const body = read(rel).replace(/^---\n[\s\S]*?\n---\n?/, '').trim();
	const id = `agent_${L}_${slug.replace(/-/g, '_')}`;
	if (!a.id || !a.name) fail(`${rel}: frontmatter needs id and name`);
	else if (a.id !== id) fail(`${rel}: id must be ${id} (is ${a.id})`);
	if ('instructions' in a) fail(`${rel}: instructions belong in the body, not in the frontmatter`);
	if (!body) fail(`${rel}: body (the instructions) is empty`);
	if ('avatar' in a) fail(`${rel}: no avatar (an uploaded avatar path only exists in the tenant it came from)`);
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

// admin/model-labels/ (label file v2, one file for every locale; see admin/model-labels/README.md)
const LABELS = 'admin/model-labels/labels.yaml';
let labelCount = 0;
for (const L of LOCALES) {
	if (existsSync(join(root, `admin/model-labels/${L}.yaml`))) fail(`admin/model-labels/${L}.yaml: v1 label files are replaced by ${LABELS}`);
}
if (!existsSync(join(root, LABELS))) fail(`${LABELS}: missing`);
else {
	let doc;
	try {
		doc = parse(read(LABELS));
	} catch (e) {
		fail(`${LABELS}: not valid YAML (${e.message.split('\n')[0]})`);
	}
	if (doc !== undefined) {
		for (const e of validateModelLabels(doc, LABELS)) fail(e);
		labelCount = Array.isArray(doc?.models) ? doc.models.length : 0;
	}
}

if (errors.length) {
	console.error(`validate: ${errors.length} problem(s):\n  - ${errors.join('\n  - ')}`);
	process.exit(1);
}
console.log(`validate: ${skillNames.size} skills, ${agents.length} agents, model labels (${labelCount} models) OK`);
