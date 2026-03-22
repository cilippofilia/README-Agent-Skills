---
name: "swift-readme"
description: "Use when the user asks to write, rewrite, improve, or restyle a README.md for an app, package, library, CLI, internal tool, or repository based on real project context. Best for creating accurate, polished READMEs from source structure, manifests, docs, assets, and examples without inventing capabilities."
---

# README Playbook For Claude Code

This is the Claude Code skill adapter for the repository's shared README playbook.

Keep this file thin. The reusable guidance lives in `../../../core/`.

## Core workflow

1. Inspect the real repository before drafting or rewriting a README.
2. Identify the repo type: app, package, library, SDK, CLI, internal tool, template, or mixed.
3. Read the current `README.md` if it exists.
4. Keep claims grounded in project files. Do not invent features, setup steps, compatibility, assets, links, translations, or contributor identities.
5. Read the relevant file from `../../../core/` before drafting.
6. Read additional core files only when the task requires them.

## Decision tree

- For apps and products, read `../../../core/apps.md`.
- For packages, libraries, frameworks, and SDKs, read `../../../core/packages.md`.
- For CLIs, scripts, generators, and internal tools, read `../../../core/tools.md`.
- For visual placement, screenshots, GIFs, videos, or sample output, read `../../../core/visual-assets.md`.
- For rewriting a stale or bloated README, read `../../../core/rewrites.md`.
- For contributor guidance or attribution, read `../../../core/contributors.md`.
- For multilingual or license-sensitive work, read `../../../core/special-cases.md`.

## Shared contract

Follow the shared rules in `../../../core/OVERVIEW.md`:

- inspect the real repo first
- identify the repo type
- load only the relevant guidance
- avoid invented claims, assets, and links
- recommend visuals only when they materially improve clarity
- add `Contributing` and `Contributors` only when relevant and verified
- prefer git-derived contributor names and verified avatars when available

## Claude-specific notes

- Install this skill by copying `.claude/skills/swift-readme/` into a repository or user-level Claude skills location.
- Trigger it by asking Claude to use the `swift-readme` skill for README work.
- Treat `../../../core/` as the source of truth for the reusable README playbook.
