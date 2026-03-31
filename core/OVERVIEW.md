# README Playbook Core

This directory contains the shared, model-agnostic guidance for writing and rewriting repository READMEs.

Use these files as the single source of truth. Platform-specific adapters such as Codex should route into this directory instead of copying the guidance.

## Adapter contract

Every adapter should follow the same behavior:

1. Inspect the real repository before drafting.
2. Identify the repo type.
3. Load only the relevant core guidance.
4. Keep claims grounded in actual project files.
5. Recommend visuals only when they materially improve clarity.
6. Add `Contributing` and `Contributors` only when relevant and verified.
7. When justified by real assets and metadata, recommend a top README block with a centered image, verified support badges, and verified contact badges.
8. When platform, language, or toolchain versions are explicit in the repo, include support badges by default rather than leaving them out.
9. When a README would benefit from future polish that cannot be completed from the current repo context, leave concise hidden guidance comments using exactly `[//]: # (...)`.

## Improvement comments

Use portable Markdown comments when the README should guide the user toward missing assets or follow-up improvements without showing that guidance in rendered output.

Rules:

- Use exactly this syntax: `[//]: # (comment text)`
- Keep comments short, specific, and actionable
- Place the comment immediately above the section it refers to
- Prefer comments for missing hero images, demo videos, screenshots, badges, diagrams, or other verifiable enhancements
- Do not use comments for filler, apologies, or generic writing advice
- Do not invent asset filenames, URLs, or claims inside the comment unless you are presenting them as clearly labeled examples

Examples:

- `[//]: # (Hero section: this would benefit from a centered image above the title, for example <p align="center"><img src="Docs/Images/hero.svg" alt="Project logo" width="60%" /></p>)`
- `[//]: # (Features section: this would benefit from a short demo video or GIF that shows the primary workflow end to end.)`

## Core files

- `apps.md` for user-facing apps and products
- `packages.md` for packages, libraries, frameworks, and SDKs
- `tools.md` for CLIs, generators, scripts, and internal tools
- `visual-assets.md` for screenshots, GIFs, videos, diagrams, and sample output
- `rewrites.md` for cleanup and restructuring of existing READMEs
- `contributors.md` for contribution guidance and contributor attribution
- `special-cases.md` for multilingual and license-sensitive work

## Authoring rule

When changing README guidance, update the relevant file in `core/` first. Adapter layers should stay thin and only describe how a specific model/runtime consumes the playbook.
