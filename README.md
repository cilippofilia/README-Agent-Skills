# README Agent Playbook

Reusable README-writing guidance for AI agents.

This repository is now structured as a model-agnostic core plus thin platform adapters. The shared guidance covers app READMEs, package READMEs, tool READMEs, visual recommendations, rewrite cleanup, contributor sections, and special cases such as multilingual docs and license-aware sections.

## Architecture

- `core/` is the source of truth for reusable README guidance
- `swift-readme/` is the Codex-specific adapter
- `claude/` contains the Claude Code adapter
- future adapters such as Claude or generic prompt packs can be added without duplicating the core guidance

## Repository Structure

```text
README-Agent-Skills/
├── README.md
├── core/
│   ├── OVERVIEW.md
│   ├── apps.md
│   ├── contributors.md
│   ├── packages.md
│   ├── rewrites.md
│   ├── special-cases.md
│   ├── tools.md
│   └── visual-assets.md
├── claude/
│   └── CLAUDE.md
└── swift-readme/
    └── SKILL.md
```

## Core Contract

All adapters should follow the same contract:

- inspect the real repository before drafting
- identify the repo type
- load only the relevant core guidance
- avoid invented claims, assets, and links
- recommend visuals only when they materially improve clarity
- add `Contributing` and `Contributors` only when relevant and verified

See [core/OVERVIEW.md](core/OVERVIEW.md) for the shared rules.

## Using With Codex

The current adapter is `swift-readme` for Codex.

Install it by copying the adapter folder into your Codex skills directory:

```bash
cp -R swift-readme ~/.codex/skills/
```

In Codex, trigger it with:

```text
$swift-readme
```

Or ask for it in natural language, for example:

- `Use the swift-readme skill to rewrite this app README.`
- `Use the swift-readme skill to improve this package README.`
- `Use the swift-readme skill to add contributor guidance and keep the license section accurate.`

## Using With Claude Code

Claude Code uses a project-level `CLAUDE.md` file for repository instructions.

This repo now includes a Claude adapter at [claude/CLAUDE.md](claude/CLAUDE.md). You can use it in either of these ways:

1. Copy [claude/CLAUDE.md](claude/CLAUDE.md) into your target repository as `CLAUDE.md` and keep the `core/` folder alongside it.
2. Import it from your target repository's root `CLAUDE.md` using an absolute path to your local clone of this playbook repo.

Example import:

```md
@/absolute/path/to/README-Agent-Skills/claude/CLAUDE.md
```

The Claude adapter follows the same core contract as the Codex adapter and routes into the shared guidance under [core/](core/).

## Current Coverage

The core playbook currently includes guidance for:

- apps and products
- packages, libraries, frameworks, and SDKs
- CLIs, scripts, generators, and internal tools
- screenshots, GIFs, videos, diagrams, and sample output
- rewriting bloated or stale READMEs
- `Contributing` and `Contributors` sections
- multilingual and license-sensitive README work

## Contributing

Contributions should improve the shared playbook or keep adapters thin and accurate.

What to contribute:

- clearer shared guidance in `core/`
- better adapter boundaries so platform-specific wrappers stay minimal
- stronger rewrite heuristics, contributor guidance, or visual-placement guidance
- new adapters that consume the core contract without duplicating it

Where to contribute:

- update files in [core/](core/) for reusable README guidance
- update [swift-readme/SKILL.md](swift-readme/SKILL.md) only for Codex-specific behavior
- update [README.md](README.md) when the repository structure or positioning changes

Why contribute:

- to keep README advice portable across models
- to reduce duplication between adapters
- to make the playbook easier to extend to Claude and other runtimes later

Keep edits factual, concise, and aligned with the shared contract in `core/OVERVIEW.md`.
