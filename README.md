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

The skill lives in [`swift-readme/SKILL.md`](swift-readme/SKILL.md).

## Repository Structure

```text
README-Agent-Skills/
├── README.md
└── swift-readme/
    └── SKILL.md
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
- choosing section order based on repo type
- avoiding invented features or stale claims
- borrowing good README patterns without copying blindly

## Inspiration

This repository structure and README pacing were inspired by [twostraws/SwiftUI-Agent-Skill](https://github.com/twostraws/SwiftUI-Agent-Skill), adapted here for a README-focused Codex skill repository.
