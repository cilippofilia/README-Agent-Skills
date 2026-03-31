# README Intake

Use this reference when repository inspection is not enough to confidently choose the README direction.

## Decision rule

Inspect the repo first. Ask questions only when repo type, audience, purpose, primary workflow, or missing proof assets are still unclear after reading the codebase, manifests, and existing docs.

Do not start every README task with an intake form.

Use `create` for new README work or when the existing README is too weak to guide the structure.
Use `update` when the repo already has a README and the main need is diagnosis, cleanup, or targeted rewriting.

## When intake helps

Use intake for cases such as:

- sparse repos with little code or no README
- mixed repos where app, package, tool, or template boundaries are unclear
- agent skills or other niche repo types where intent is not obvious from files alone
- rewrites where the current README does not explain who it is for or why it exists
- repos where proof assets, contact metadata, or launch instructions are missing from the codebase

## Repo type taxonomy

Use one of these types unless the user gives a better label:

- `app`: user-facing product or application
- `package-library`: reusable package, library, framework, plugin, or SDK
- `cli-tool`: command line tool, automation, generator, script collection, or internal utility
- `template`: starter repo, boilerplate, example app, or scaffold
- `docs-site`: documentation-first or content-first repo
- `agent-skill`: installable skill, agent playbook, or AI workflow bundle
- `mixed-other`: mixed repo or repo that does not fit the above cleanly

## Core questions

Ask only the smallest missing subset needed to write a better README.

Core questions:

1. What repo type best describes this project?
2. Who is the README for?
3. What should the reader understand in the first screenful?
4. What is the primary action the reader should take after opening the README?
5. Why does this project exist, beyond what the code already shows?
6. Which proof assets matter most: screenshot, GIF, video, sample output, diagram, none, or unknown?
7. Are there constraints or preferences for tone, ordering, or sections?

## Type-specific follow-ups

### App

- What user problem does the app solve?
- Which platforms matter most to call out?
- Should the README sell the product, explain setup, or balance both?

### Package or library

- What integration path should appear first?
- What is the smallest useful example?
- Is this for public developers, internal teams, or both?

### CLI or tool

- What input produces the most representative successful run?
- What output or artifact proves the tool worked?
- Is this public-facing or internal-only?

### Template

- What should users build from this starter?
- What should they replace or customize first?
- Does the README need onboarding steps or just orientation?

### Docs site

- Is the README a landing page, a maintainer guide, or a local-dev guide?
- Should it direct readers into published docs quickly?

### Agent skill

- What kinds of user prompts should trigger this skill?
- What task does the skill help another agent perform repeatedly?
- Is the README for skill users, skill maintainers, or both?

### Mixed or other

- Which part of the repo matters most to a new reader?
- Should the README frame the repo as one product, or as multiple related pieces?

## Intake output

When intake is needed, summarize answers as a compact Markdown brief with these sections:

- `## Repo Type`
- `## Audience`
- `## Purpose`
- `## Primary User Journey`
- `## Verified Metadata`
- `## Missing Assets Or Proof`
- `## Constraints Or Preferences`
- `## Notes For README`

Use this brief as source-of-truth context for the README task. Keep it concise and factual.

For `update`, keep the same section headings but include rewrite-specific notes such as:

- what is wrong with the current README
- what must stay
- what is missing now
- whether the user wants a rewrite, cleanup, or focused improvement

## Questioning style

- Ask in stages, not all at once
- Prefer repo-type and audience first
- Skip questions that inspection already answered
- Avoid asking for facts that are clearly present in manifests or source files
- If the user provides weak or partial answers, reflect that uncertainty in the brief instead of inventing details
