# Package READMEs

Use this reference for packages, libraries, frameworks, SDKs, and reusable modules.

## Priorities

1. Get the reader to install or integrate the package quickly.
2. Show the smallest useful example early.
3. Explain compatibility, entry points, and core concepts without over-documenting internals.

## Recommended section order

- Title
- About
- Installation or Getting Started
- Usage
- Examples
- Requirements or Compatibility
- Project Structure or Concepts
- Contributing
- Contributors or License

For package repos, quick start usually matters more than a long feature list.

## What good package READMEs do

- Include copy-pasteable install instructions.
- Show the first successful usage path near the top.
- Explain what problem the package solves for developers.
- Use examples that map to real API entry points.
- Separate conceptual depth from onboarding.

## Visual guidance

Many package READMEs do not need screenshots. Prefer:

- code examples for APIs
- diagrams only when they simplify a non-obvious concept
- sample output when the package generates artifacts or console output

Use [visual-assets.md](visual-assets.md) only when a visual genuinely explains the package faster than text or code.

## Common mistakes

- Burying installation below architecture
- Writing examples that do not match the real API
- Treating low-level implementation details as onboarding content
- Adding screenshots where code would be clearer
- Inventing compatibility claims or package manager instructions

## Contributor sections

Package READMEs often benefit from explicit contribution guidance. When supported by the repo, add:

- a `Contributing` section that explains what kinds of contributions are useful, where contributors should edit, and why those areas matter
- a `Contributors` section near the bottom when contributor names are verified from the repository
