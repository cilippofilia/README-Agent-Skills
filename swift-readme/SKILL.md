---
name: "swift-readme"
description: "Use when the user asks to write, rewrite, improve, or restyle a README.md for an app, package, library, CLI, internal tool, or repository based on real project context. Best for creating accurate, polished READMEs from source structure, manifests, docs, assets, and examples without inventing capabilities."
---

# Swift README

Use this skill to create or improve README files from verified repository context.

Keep this file as the router. Load only the reference files that match the repository type and task.

## Core workflow

1. Identify the repo type before drafting: app, package, library, SDK, CLI, internal tool, template, or mixed.
2. Read the current `README.md` if it exists.
3. Inspect the real project context: manifests, entry points, source tree, tests, docs, assets, examples, and license files.
4. Verify claims against the codebase. Never invent features, setup steps, compatibility, screenshots, links, or translations.
5. Choose the relevant reference file for the repo type.
6. Draft or rewrite the README around the fastest path to reader understanding.
7. Check whether visuals or sample output would materially improve clarity. Recommend them only when justified.

## Workflow decision tree

### 1) App or product README

Read [references/apps.md](references/apps.md).

Use for:

- iOS, macOS, web, or desktop apps
- user-facing products
- repos where visual proof and feature positioning matter early

### 2) Package, library, framework, or SDK README

Read [references/packages.md](references/packages.md).

Use for:

- Swift packages
- developer libraries
- frameworks, SDKs, plugins, and reusable modules

### 3) CLI, internal tool, automation, or utility README

Read [references/tools.md](references/tools.md).

Use for:

- CLIs
- build tools
- generators
- scripts
- internal workflows and operational utilities

### 4) Visual placement or demo decisions

Read [references/visual-assets.md](references/visual-assets.md) when:

- the repo contains screenshots, videos, GIFs, sample output, or demos
- the README would be clearer with visual proof
- you need to recommend a missing asset without inventing it

### 5) Rewrite-heavy cleanup

Read [references/rewrites.md](references/rewrites.md) when:

- an existing README is bloated, stale, duplicated, or poorly ordered
- the user wants a rewrite rather than a new draft
- you need a cleanup checklist before editing

### 6) Multilingual or license-sensitive README work

Read [references/special-cases.md](references/special-cases.md) when:

- the user asks for translated README support
- translated README files already exist
- the user asks for a specific license section style
- the repo has a license file that the README should reflect

### 7) Contributor guidance or attribution

Read [references/contributors.md](references/contributors.md) when:

- the user asks for a `Contributing` section
- the user asks for a `Contributors` section
- you need to decide whether contributor guidance should be included

## Universal rules

- Explain what the project is and why it matters before deep details.
- Help the reader reach a successful first result quickly.
- Keep onboarding steps minimal and executable.
- Match the README structure to the repo type instead of forcing a template.
- Add a `Contributing` section when the repository would benefit from contribution guidance.
- Add a `Contributors` section near the bottom when contributor information is available and relevant.
- Prefer concrete examples over generic marketing copy.
- Place architecture and implementation details after comprehension and first-run guidance.
- Preserve correct existing facts; remove stale or vague text.
- Keep translated README structure and license sections aligned with what the repo actually contains.

## Inspection checklist

Inspect only what is useful:

- `README.md`
- `LICENSE`, `LICENSE.md`, or equivalent
- translated README files, if present or requested
- manifests such as `Package.swift`, `*.xcodeproj`, `*.xcworkspace`, `package.json`, `pyproject.toml`, `Cargo.toml`
- app entry points and main modules
- source layout
- tests
- docs
- assets, screenshots, screen recordings, or sample output
- examples, sample apps, or starter templates
- git history or existing contributor mentions, if you need to verify contributors

## Output standard

The finished README should be:

- accurate
- specific to the repo
- easy to scan
- stronger than boilerplate
- useful within the first screenful

If the repo lacks assets but the README would clearly benefit from them, include a short recommendation in the relevant section or in a concise follow-up note. Do not invent files or links.
