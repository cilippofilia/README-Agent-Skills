# Package READMEs

Use this reference for packages, libraries, frameworks, SDKs, and reusable modules.

## Priorities

1. Get the reader to install or integrate the package quickly.
2. Show the smallest useful example early.
3. Explain compatibility, entry points, and core concepts without over-documenting internals.
4. Surface verified compatibility near the top when the manifest or project files state it clearly.

## Recommended section order

- Title
- About
- Installation or Getting Started
- Usage
- Examples
- Requirements or Compatibility
- Project Structure or Concepts
- License

For package repos, quick start usually matters more than a long feature list.

## What good package READMEs do

- Include copy-pasteable install instructions.
- Use `header.md` when the package README needs a top block with brand or compatibility context.
- Show the first successful usage path near the top.
- Explain what problem the package solves for developers.
- Use examples that map to real API entry points.
- Separate conceptual depth from onboarding.
- Prefer badges for Swift and platform support when `Package.swift` or Xcode metadata makes those versions explicit.

## Visual guidance

Many package READMEs do not need screenshots. Prefer:

- a top logo or package pill above the title when the repo already has a strong visual asset
- compatibility badges for supported OS versions, Swift versions, or ecosystems when those claims can be verified
- a contact badge only when the maintainer link or handle is explicit in the repo or provided by the user
- code examples for APIs
- diagrams only when they simplify a non-obvious concept
- sample output when the package generates artifacts or console output

Use [header.md](header.md) for header composition. Use [visual-assets.md](visual-assets.md) only when a non-header visual genuinely explains the package faster than text or code.

## Common mistakes

- Burying installation below architecture
- Writing examples that do not match the real API
- Treating low-level implementation details as onboarding content
- Adding screenshots where code would be clearer
- Inventing compatibility claims or package manager instructions
