# README Agent Playbook

Reusable README-writing guidance for AI agents.

This repository is structured as a model-agnostic core plus thin platform adapters. The shared guidance covers app READMEs, package READMEs, tool READMEs, visual recommendations, rewrite cleanup, contributor sections, and special cases such as multilingual docs and license-aware sections.

## Architecture

- `core/` is the source of truth for reusable README guidance
- `skills/swift-readme/` is the installable Codex skill
- `.claude/skills/swift-readme/` is the installable Claude skill
- `CLAUDE.md` is the root Claude Code adapter for this repository
- future adapters can be added without duplicating the core guidance

## Repository Structure

```text
README-Agent-Skills/
├── CLAUDE.md
├── .claude/
│   └── skills/
│       └── swift-readme/
│           └── SKILL.md
├── README.md
├── skills/
│   └── swift-readme/
│       └── SKILL.md
└── core/
    ├── OVERVIEW.md
    ├── apps.md
    ├── contributors.md
    ├── packages.md
    ├── rewrites.md
    ├── special-cases.md
    ├── tools.md
    └── visual-assets.md
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

## Install With npx

This repository now exposes its Codex skill from the standard `skills/` discovery path, so it can be installed directly with the Skills CLI:

```bash
npx skills add cilippofilia/README-Agent-Skills --skill swift-readme
```

That matches the repository layout expected by `npx skills` for GitHub-hosted skill repos.

## Using With Codex

The current Codex adapter is `swift-readme`.

Install it with `npx skills`, or copy the skill folder into your Codex skills directory manually:

```bash
cp -R skills/swift-readme ~/.codex/skills/
```

In Codex, trigger it with:

```text
$swift-readme
```

Or ask for it in natural language, for example:

- `Use the swift-readme skill to rewrite this app README.`
- `Use the swift-readme skill to improve this package README.`
- `Use the swift-readme skill to add contributor guidance and keep the license section accurate.`

## Why This Layout

The `npx skills` CLI looks for skills in standard repository locations such as `skills/` and `.agents/skills/`. Keeping the installable adapter in `skills/swift-readme/` makes this repo align with the broader Agent Skills ecosystem and avoids depending on recursive fallback discovery.

## Using With Claude Code

This repository now supports Claude in the paths Claude expects:

- [CLAUDE.md](/Users/filippocilia/Desktop/Projects/Packages/README-Agent-Skills/CLAUDE.md) for automatic repository-level loading
- [.claude/skills/swift-readme/SKILL.md](/Users/filippocilia/Desktop/Projects/Packages/README-Agent-Skills/.claude/skills/swift-readme/SKILL.md) for Claude skill-style installation

If you want to reuse the repository-level adapter elsewhere, copy [CLAUDE.md](/Users/filippocilia/Desktop/Projects/Packages/README-Agent-Skills/CLAUDE.md) into your target repository as `CLAUDE.md` and keep the `core/` folder alongside it.

If you want the reusable Claude skill, copy `.claude/skills/swift-readme/` into the corresponding Claude skills location for the target environment.

Both Claude entry points follow the same core contract and route into the shared guidance under [core/](core/).

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
- update [skills/swift-readme/SKILL.md](skills/swift-readme/SKILL.md) only for Codex-specific behavior
- update [README.md](README.md) when the repository structure or positioning changes

Why contribute:

- to keep README advice portable across models
- to reduce duplication between adapters
- to make the playbook easier to extend to Claude and other runtimes later

Keep edits factual, concise, and aligned with the shared contract in `core/OVERVIEW.md`.
