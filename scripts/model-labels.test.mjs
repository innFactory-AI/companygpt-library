// Self-test for the label file v2 checks: node --test scripts/model-labels.test.mjs (npm test)
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { spawnSync } from 'node:child_process';
import { mkdirSync, mkdtempSync, readFileSync, rmSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { parse, stringify } from 'yaml';
import { validateModelLabels } from './model-labels.mjs';

const REL = 'labels.yaml';

// A small, valid label file; each test breaks one thing in a fresh copy.
function validDoc() {
	return {
		version: 2,
		locales: ['de', 'en'],
		groups: [
			{ id: 'openai', label: 'OpenAI', icon: 'openAI' },
			{ id: 'stackit', label: { de: 'STACKIT', en: 'STACKIT' }, icon: 'https://example.com/stackit.svg' },
		],
		models: [
			{
				model: 'gpt-6.1-sol',
				group: 'openai',
				menu: 'featured',
				supersededBy: [],
				aliases: ['gpt-61-sol'],
				endpoints: ['openAI', 'azureOpenAI'],
				label: { de: 'GPT-6.1 Sol', en: 'GPT-6.1 Sol' },
				description: { de: 'Stärkstes GPT', en: 'Strongest GPT' },
			},
			{
				model: 'gpt-6-sol',
				group: 'openai',
				supersededBy: ['gpt-6.1-sol'],
				label: { de: 'GPT-6 Sol', en: 'GPT-6 Sol' },
			},
			{ model: 'gpt-oss-120b', group: 'stackit', menu: 'available', label: { de: 'GPT-OSS 120B', en: 'GPT-OSS 120B' } },
		],
	};
}

const errorsOf = (doc) => validateModelLabels(doc, REL);
function assertFails(doc, ...needles) {
	const errors = errorsOf(doc);
	assert.ok(errors.length > 0, 'expected at least one error');
	for (const n of needles) {
		assert.ok(
			errors.some((e) => e.includes(n)),
			`expected an error containing ${JSON.stringify(n)}, got:\n  ${errors.join('\n  ')}`,
		);
	}
	for (const e of errors) assert.ok(e.startsWith(`${REL}: `), `error must name the file: ${e}`);
}

test('a valid v2 file passes', () => {
	assert.deepEqual(errorsOf(validDoc()), []);
});

test('version must be 2', () => {
	for (const v of [1, '2', undefined, 3]) {
		const d = validDoc();
		d.version = v;
		assertFails(d, 'version');
	}
});

test('an empty or non-object document fails', () => {
	assertFails(null, 'version');
	assertFails([], 'version');
});

test('unknown top-level key is rejected', () => {
	const d = validDoc();
	d.labels = [];
	assertFails(d, 'unknown key "labels"');
});

test('unknown group key is rejected and names the group', () => {
	const d = validDoc();
	d.groups[0].groupIcon = 'openAI';
	assertFails(d, 'groups[openai]: unknown key "groupIcon"');
});

test('unknown model key is rejected and names the model', () => {
	const d = validDoc();
	d.models[1].price = 3;
	assertFails(d, 'gpt-6-sol: unknown key "price"');
});

test('unknown locale key in a text is rejected', () => {
	const d = validDoc();
	d.models[0].label.fr = 'GPT-6.1 Sol';
	assertFails(d, 'gpt-6.1-sol: label: unknown key "fr"');
});

test('menu must be featured or available', () => {
	const d = validDoc();
	d.models[2].menu = 'hidden';
	assertFails(d, 'gpt-oss-120b: menu');
});

test('a model id listed twice is rejected', () => {
	const d = validDoc();
	d.models.push({ model: 'gpt-6-sol', group: 'openai', label: { de: 'x', en: 'x' } });
	assertFails(d, 'gpt-6-sol: id "gpt-6-sol" is used twice');
});

test('an alias that equals another model id is rejected', () => {
	const d = validDoc();
	d.models[2].aliases = ['gpt-6-sol'];
	assertFails(d, 'gpt-oss-120b: id "gpt-6-sol" is used twice');
});

test('an alias used by two models is rejected', () => {
	const d = validDoc();
	d.models[1].aliases = ['gpt-61-sol'];
	assertFails(d, 'gpt-6-sol: id "gpt-61-sol" is used twice');
});

test('a model id must be a non-empty string', () => {
	const d = validDoc();
	d.models[2].model = '';
	assertFails(d, 'models[2]: model');
});

test('a model referencing an unknown group is rejected', () => {
	const d = validDoc();
	d.models[2].group = 'ionos';
	assertFails(d, 'gpt-oss-120b: unknown group "ionos"');
});

test('a model without group is rejected', () => {
	const d = validDoc();
	delete d.models[2].group;
	assertFails(d, 'gpt-oss-120b: unknown group');
});

test('a group id listed twice is rejected', () => {
	const d = validDoc();
	d.groups.push({ id: 'openai', label: 'OpenAI 2' });
	assertFails(d, 'groups[openai]: id "openai" is used twice');
});

test('a group needs an id and a label', () => {
	const d = validDoc();
	d.groups.push({ icon: 'google' });
	assertFails(d, 'groups[2]: id', 'groups[2]: label');
});

test('a group icon must be a non-empty string', () => {
	const d = validDoc();
	d.groups[0].icon = '';
	assertFails(d, 'groups[openai]: icon');
});

test('an unknown successor is rejected', () => {
	const d = validDoc();
	d.models[1].supersededBy = ['gpt-7'];
	assertFails(d, 'gpt-6-sol: supersededBy: unknown model "gpt-7"');
});

test('an alias is not a valid successor (successors are model ids)', () => {
	const d = validDoc();
	d.models[1].supersededBy = ['gpt-61-sol'];
	assertFails(d, 'gpt-6-sol: supersededBy: unknown model "gpt-61-sol"');
});

test('a model superseded by itself is a cycle', () => {
	const d = validDoc();
	d.models[2].supersededBy = ['gpt-oss-120b'];
	assertFails(d, 'gpt-oss-120b: supersededBy has a cycle');
});

test('a successor cycle over several models is rejected', () => {
	const d = validDoc();
	d.models[0].supersededBy = ['gpt-oss-120b'];
	d.models[2].supersededBy = ['gpt-6-sol'];
	assertFails(d, 'supersededBy has a cycle', 'gpt-6.1-sol -> gpt-oss-120b -> gpt-6-sol -> gpt-6.1-sol');
});

test('supersededBy must be a list', () => {
	const d = validDoc();
	d.models[1].supersededBy = 'gpt-6.1-sol';
	assertFails(d, 'gpt-6-sol: supersededBy must be a list');
});

test('a diamond (two paths to one successor) is not a cycle', () => {
	const d = validDoc();
	d.models[2].supersededBy = ['gpt-6-sol', 'gpt-6.1-sol'];
	assert.deepEqual(errorsOf(d), []);
});

test('locales must be a non-empty list of unique locale codes', () => {
	for (const v of [undefined, [], ['de', 'de'], 'de', ['de', '']]) {
		const d = validDoc();
		d.locales = v;
		assertFails(d, 'locales');
	}
});

test('a missing locale label is rejected and names the model and locale', () => {
	const d = validDoc();
	delete d.models[1].label.en;
	assertFails(d, 'gpt-6-sol: label.en is missing');
});

test('a model without label is rejected', () => {
	const d = validDoc();
	delete d.models[2].label;
	assertFails(d, 'gpt-oss-120b: label');
});

test('a missing locale description is rejected', () => {
	const d = validDoc();
	delete d.models[0].description.de;
	assertFails(d, 'gpt-6.1-sol: description.de is missing');
});

test('a missing locale in a group label map is rejected', () => {
	const d = validDoc();
	delete d.groups[1].label.en;
	assertFails(d, 'groups[stackit]: label.en is missing');
});

test('an empty label is rejected', () => {
	const d = validDoc();
	d.models[1].label.de = '';
	assertFails(d, 'gpt-6-sol: label.de is empty');
	const g = validDoc();
	g.groups[0].label = '  ';
	assertFails(g, 'groups[openai]: label is empty');
});

test('a label of 128 characters passes, 129 is rejected', () => {
	const ok = validDoc();
	ok.models[1].label.de = 'x'.repeat(128);
	assert.deepEqual(errorsOf(ok), []);
	const d = validDoc();
	d.models[1].label.de = 'x'.repeat(129);
	assertFails(d, 'gpt-6-sol: label.de is longer than 128 characters');
});

test('a label with control characters is rejected', () => {
	for (const bad of ['GPT\n6', 'GPT\t6', 'GPT\u00076', 'GPT\u007f6']) {
		const d = validDoc();
		d.models[1].label.en = bad;
		assertFails(d, 'gpt-6-sol: label.en contains control characters');
	}
});

test('a non-string label is rejected', () => {
	const d = validDoc();
	d.models[1].label.en = 6;
	assertFails(d, 'gpt-6-sol: label.en must be a string');
});

test('a description of 120 characters passes, 121 is rejected', () => {
	const ok = validDoc();
	ok.models[0].description.en = 'y'.repeat(120);
	assert.deepEqual(errorsOf(ok), []);
	const d = validDoc();
	d.models[0].description.en = 'y'.repeat(121);
	assertFails(d, 'gpt-6.1-sol: description.en is longer than 120 characters');
});

test('a model label must be a map per locale, not a plain string', () => {
	const d = validDoc();
	d.models[2].label = 'GPT-OSS 120B';
	assertFails(d, 'gpt-oss-120b: label: must be a map');
});

test('groups and models must be lists', () => {
	const d = validDoc();
	d.groups = {};
	d.models = undefined;
	assertFails(d, 'groups must be a list', 'models must be a list');
});

test('endpoints must be a list of unique non-empty strings', () => {
	const d = validDoc();
	d.models[0].endpoints = 'openAI';
	assertFails(d, 'gpt-6.1-sol: endpoints must be a list');
	const dup = validDoc();
	dup.models[0].endpoints = ['openAI', 'openAI'];
	assertFails(dup, 'gpt-6.1-sol: endpoints lists "openAI" twice');
});

test('the library label file passes', () => {
	const rel = 'admin/model-labels/labels.yaml';
	const doc = parse(readFileSync(new URL(`../${rel}`, import.meta.url), 'utf8'));
	assert.deepEqual(validateModelLabels(doc, rel), []);
});

const VALIDATE = fileURLToPath(new URL('./validate.mjs', import.meta.url));
const runValidate = (root) => spawnSync(process.execPath, [VALIDATE, root], { encoding: 'utf8' });

test('npm run validate passes on the library', () => {
	const r = runValidate(fileURLToPath(new URL('..', import.meta.url)));
	assert.equal(r.status, 0, r.stderr);
	assert.match(r.stdout, /model labels \(\d+ models\) OK/);
});

// A minimal repo root with only a catalog and the given model-labels files.
function fixtureRoot(files) {
	const root = mkdtempSync(join(tmpdir(), 'label-file-validation-'));
	const index = { title: 't', description: 'd', intro: 'i' };
	writeFileSync(join(root, 'catalog.json'), JSON.stringify({ categories: [], index: { de: index, en: index } }));
	mkdirSync(join(root, 'admin/model-labels'), { recursive: true });
	for (const [name, content] of Object.entries(files)) writeFileSync(join(root, 'admin/model-labels', name), content);
	return root;
}

test('npm run validate fails on a broken label file and names the entry', (t) => {
	const d = validDoc();
	d.models[1].supersededBy = ['gpt-7'];
	const root = fixtureRoot({ 'labels.yaml': stringify(d) });
	t.after(() => rmSync(root, { recursive: true, force: true }));
	const r = runValidate(root);
	assert.equal(r.status, 1);
	assert.match(r.stderr, /admin\/model-labels\/labels\.yaml: gpt-6-sol: supersededBy: unknown model "gpt-7"/);
});

test('npm run validate rejects leftover v1 files and a missing labels.yaml', (t) => {
	const root = fixtureRoot({ 'de.yaml': 'labels: []\n' });
	t.after(() => rmSync(root, { recursive: true, force: true }));
	const r = runValidate(root);
	assert.equal(r.status, 1);
	assert.match(r.stderr, /admin\/model-labels\/de\.yaml: v1 label files are replaced/);
	assert.match(r.stderr, /admin\/model-labels\/labels\.yaml: missing/);
});

test('npm run validate reports invalid YAML', (t) => {
	const root = fixtureRoot({ 'labels.yaml': 'version: 2\nmodels: [\n' });
	t.after(() => rmSync(root, { recursive: true, force: true }));
	const r = runValidate(root);
	assert.equal(r.status, 1);
	assert.match(r.stderr, /labels\.yaml: not valid YAML/);
});
