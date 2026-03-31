---
name: "swift-readme"
description: "Use when the user asks to write, rewrite, improve, or restyle a README.md for an app, package, library, CLI, internal tool, or repository based on real project context. Best for creating accurate, polished READMEs from source structure, manifests, docs, assets, and examples without inventing capabilities."
---

# Swift README For Codex

This is the Codex adapter for the repository's shared README playbook.

Keep this file thin. The reusable guidance lives in `../../core/`.

## Codex workflow

1. Identify the repo type before drafting: app, package, library, SDK, CLI, internal tool, template, or mixed.
2. Read the current `README.md` if it exists.
3. Inspect the real project context: manifests, entry points, source tree, tests, docs, assets, examples, and license files.
4. Verify claims against the codebase. Never invent features, setup steps, compatibility, screenshots, links, or translations.
5. When supported versions are explicit in high-confidence project metadata, include support badges by default near the top of the README.
6. When a missing asset or proof materially hurts clarity or trust, leave a hidden guidance comment using exactly `[//]: # (...)` above the relevant section.
7. Read `../../core/header.md` whenever you are shaping the top of the README, deciding badge policy, or considering hidden improvement comments.
8. Load the matching file from `../../core/`.
9. Draft or rewrite the README around the fastest path to reader understanding.
10. If multiple topics apply, load only the additional core files you need.

## Workflow decision tree

### 1) App or product README

Read [../../core/apps.md](../../core/apps.md).

Use for:

- iOS, macOS, web, or desktop apps
- user-facing products
- repos where visual proof and feature positioning matter early

### 2) Package, library, framework, or SDK README

Read [../../core/packages.md](../../core/packages.md).

Use for:

- Swift packages
- developer libraries
- frameworks, SDKs, plugins, and reusable modules

### 3) CLI, internal tool, automation, or utility README

Read [../../core/tools.md](../../core/tools.md).

Use for:

- CLIs
- build tools
- generators
- scripts
- internal workflows and operational utilities

### 4) Visual placement or demo decisions

Read [../../core/visual-assets.md](../../core/visual-assets.md) when:

- the repo contains screenshots, videos, GIFs, sample output, or demos
- the README would be clearer with visual proof
- you need to recommend a missing asset without inventing it
- you need to decide where non-header media should sit in the README

### 5) Rewrite-heavy cleanup

Read [../../core/rewrites.md](../../core/rewrites.md) when:

- an existing README is bloated, stale, duplicated, or poorly ordered
- the user wants a rewrite rather than a new draft
- you need a cleanup checklist before editing

### 6) Multilingual or license-sensitive README work

Read [../../core/special-cases.md](../../core/special-cases.md) when:

- the user asks for translated README support
- translated README files already exist
- the user asks for a specific license section style
- the repo has a license file that the README should reflect

### 7) Contributor guidance or attribution

Read [../../core/contributors.md](../../core/contributors.md) when:

- the user asks for a `Contributing` section
- the user asks for a `Contributors` section
- you need to decide whether contributor guidance should be included

### 8) Header composition or canonical examples

Read [../../core/header.md](../../core/header.md) when:

- you need to decide whether a logo or pill should sit above the title
- you need to source support badges from project metadata
- you need to decide whether a contact badge is justified
- you need to decide whether a hidden improvement comment should appear

Read [../../core/examples.md](../../core/examples.md) when:

- you want a canonical example of a polished README top section
- you need a short model for an Apple app, package, or CLI README

## Codex-specific notes

- Install this skill with `npx skills add <repo> --skill swift-readme`, or copy `skills/swift-readme/` into your Codex skills directory manually.
- Trigger it with `$swift-readme` or by asking Codex to use the `swift-readme` skill.
- Treat `../../core/` as the source of truth for README guidance.
- Do not duplicate shared guidance in this adapter unless Codex-specific behavior requires it.
- For hidden README guidance, always use the exact syntax `[//]: # (...)`.

## Shared contract

Follow the contract described in [../../core/OVERVIEW.md](../../core/OVERVIEW.md):

- inspect real repo context first
- identify the repo type
- load only the relevant core guidance
- avoid invented claims, assets, and links
- recommend visuals only when justified
- include support badges from high-confidence sources by default
- use hidden comments selectively, not as routine polish
- include contributor sections only when relevant and verified, using git-derived names and avatars when available
