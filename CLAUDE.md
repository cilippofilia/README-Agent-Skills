# README Playbook For Claude Code

Use this file as a thin Claude Code adapter for the shared README playbook.

This adapter assumes the reusable guidance lives in the sibling `core/` directory. Keep this file short and use the shared playbook as the source of truth.

## Core workflow

1. Inspect the real repository before drafting or rewriting a README.
2. Identify the repo type: app, package, library, SDK, CLI, internal tool, template, or mixed.
3. Read the current `README.md` if it exists.
4. Keep claims grounded in project files. Do not invent features, setup steps, compatibility, assets, or links.
5. If repo type, audience, purpose, or primary user journey are still unclear after inspection, read `core/intake.md` and gather only the smallest missing set of answers.
6. When supported versions are explicit in high-confidence project metadata, include support badges by default near the top of the README.
7. When a missing asset or proof materially hurts clarity or trust, leave a hidden guidance comment using exactly `[//]: # (...)` above the relevant section.
8. Read `core/header.md` whenever you are shaping the top of the README, deciding badge policy, or considering hidden improvement comments.
9. Read the relevant file from `core/` before drafting.
10. Read additional core files only when the task requires them.

## Decision tree

- For apps and products, read `core/apps.md`.
- For packages, libraries, frameworks, and SDKs, read `core/packages.md`.
- For CLIs, scripts, generators, and internal tools, read `core/tools.md`.
- For visual placement, screenshots, GIFs, videos, or sample output below the header, read `core/visual-assets.md`.
- For rewriting a stale or bloated README, read `core/rewrites.md`.
- For multilingual or license-sensitive work, read `core/special-cases.md`.
- For staged README questioning or intake briefs, read `core/intake.md`, using the `create` mental model for new drafts and the `update` mental model for rewrites.
- For top-of-README composition, badge sourcing, contact badges, or hidden improvement comments, read `core/header.md`.
- For canonical README examples, read `core/examples.md`.

## Shared contract

Follow the shared rules in `core/OVERVIEW.md`:

- inspect the real repo first
- identify the repo type
- load only the relevant guidance
- avoid invented claims, assets, and links
- recommend visuals only when they materially improve clarity
- use staged intake only when repo inspection leaves important README direction unclear
- include support badges from high-confidence sources by default
- use hidden comments selectively, not as routine polish

## Claude-specific notes

- Claude Code loads a project `CLAUDE.md` automatically when started in a repository.
- Keep this adapter concise so it remains effective as project memory.
- For reusable Claude skill installation, use `.claude/skills/swift-readme/`.
