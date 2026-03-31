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
7. Use `header.md` for top-of-README policy, including hero images, support badges, contact badges, and hidden improvement comments.
8. Include support badges by default when platform, language, or toolchain versions are explicit in a high-confidence source.
9. Use hidden improvement comments selectively with the exact `[//]: # (...)` syntax only when missing assets or proof materially hurt clarity or trust.

## Core files

- `header.md` for top-of-README composition, badge policy, contact badges, and hidden comments
- `apps.md` for user-facing apps and products
- `packages.md` for packages, libraries, frameworks, and SDKs
- `tools.md` for CLIs, generators, scripts, and internal tools
- `visual-assets.md` for screenshots, GIFs, videos, diagrams, and sample output
- `examples.md` for canonical README top-section examples
- `rewrites.md` for cleanup and restructuring of existing READMEs
- `contributors.md` for contribution guidance and contributor attribution
- `special-cases.md` for multilingual and license-sensitive work

## Authoring rule

When changing README guidance, update the relevant file in `core/` first. Adapter layers should stay thin and only describe how a specific model/runtime consumes the playbook.
