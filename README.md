# README Agent Skills

Agent skills for writing and improving repository README files with Codex.

This repository currently contains `swift-readme`, a skill for creating accurate, polished README files from real project context. It is designed to help with new README creation, README rewrites, multilingual README structure when explicitly requested, and license-aware README sections.

## Included Skills

### `swift-readme`

Use this skill when you want Codex to:

- write a new `README.md` from a real codebase
- rewrite an existing README to improve clarity and structure
- keep README claims grounded in actual project files
- handle multilingual README layouts when requested
- handle MIT-style README license sections when requested
- detect where a screenshot, GIF, video, or sample output would improve the README

The skill lives in [`swift-readme/SKILL.md`](swift-readme/SKILL.md).

It now uses a router-style `SKILL.md` plus focused reference files for app READMEs, package READMEs, tool READMEs, visual asset recommendations, rewrite cleanup, and special cases such as multilingual docs and license sections.

## Repository Structure

```text
README-Agent-Skills/
├── README.md
└── swift-readme/
    ├── SKILL.md
    └── references/
        ├── apps.md
        ├── contributors.md
        ├── packages.md
        ├── rewrites.md
        ├── special-cases.md
        ├── tools.md
        └── visual-assets.md
```

## Installing `swift-readme`

Clone this repository wherever you keep local projects, then copy the skill into your Codex skills directory:

```bash
cp -R swift-readme ~/.codex/skills/
```

If you already have a `swift-readme` folder there, replace it only if you want this repository’s version to be the source of truth.

## Using `swift-readme`

In Codex, trigger the skill with:

```text
$swift-readme
```

Or call it in natural language, for example:

- `Use the swift-readme skill to rewrite this app README.`
- `Use the swift-readme skill to create a multilingual README structure.`
- `Use the swift-readme skill to improve this package README and keep the MIT license section accurate.`

## What The Skill Focuses On

- reading the actual repository before drafting
- keeping setup steps executable and minimal
- routing guidance by repo type instead of forcing one long document
- avoiding invented features or stale claims
- recommending visuals only when they clarify the reader journey
- borrowing good README patterns without copying blindly

## Contributing

Contributions should improve the skill in a way that makes README generation more accurate, easier to follow, or easier to maintain.

What to contribute:

- clearer routing or decision logic in `swift-readme/SKILL.md`
- better repo-type guidance in `swift-readme/references/`
- tighter examples and rewrite heuristics
- visual-placement guidance that improves README clarity without encouraging invented assets

Where to contribute:

- update [swift-readme/SKILL.md](swift-readme/SKILL.md) for top-level workflow changes
- update files in [swift-readme/references/](swift-readme/references/) for topic-specific guidance
- update [README.md](README.md) when the repository structure or installation flow changes

Why contribute:

- to make the skill easier to trigger and safer to use
- to keep README advice grounded in real repository context
- to improve readability so the skill stays maintainable as it grows

Before opening changes, keep edits factual, concise, and consistent with the repository's current structure.

## Contributors

- Filippo Cilia
