---
name: "swift-readme"
description: "Use when the user asks to write, rewrite, improve, or restyle a README.md for an app, library, internal tool, or repository based on real project context. Best for creating high-quality README files from source structure, existing docs, and reference READMEs without inventing capabilities."
---

# Swift README

Create strong README files from actual repository context. This skill is for two main jobs:

- Write a new README from the codebase, project structure, and product purpose.
- Rewrite an existing README to improve clarity, structure, positioning, onboarding, and polish while keeping it accurate.

## Quick start

1. Identify the repo type: app, library, internal tool, template, or mixed.
2. Read the current `README.md` if it exists.
3. Inspect the real project context before drafting: entry points, folder structure, package or project files, tests, resources, and any user-provided reference README.
4. Infer only what the code and files support. Do not invent features, platforms, dependencies, architecture, or setup steps.
5. If the user asks for multilingual README support or a specific license style, inspect the current docs and license files before drafting.
6. Draft a README that is specific, readable, and appropriately scoped for the repository.

## Core principle

A strong README should do three things in order:

1. Explain what this project is and why it matters.
2. Help the reader get to a successful first result quickly.
3. Only then expand into deeper structure, examples, and maintenance details.

This ordering matters. Do not bury the first-run path under architecture, long feature lists, or repository trivia.

## Default title rule

Prefer an explicit product name in the title. If a tagline helps, use this pattern:

`# ProductName: Short tagline`

Avoid title-only taglines that hide the project name unless the user explicitly wants that style.

## Default structure

Use this structure when it fits the project:

- Title
- About
- Features
- Tech Stack
- Architecture or Project Structure
- Requirements
- Getting Started
- Usage, if relevant
- Development Notes, if relevant
- Author, License, or Support, if relevant

Do not force every section. For smaller repos, a shorter README is better than padded sections.

## Ordering guidance

Default section order is not always the best reading order.

- For apps and products, `About` and `Features` usually come first.
- For libraries, frameworks, CLIs, and developer tools, move `Getting Started` near the top so readers can install and try it immediately.
- Put architecture and folder structure after the reader can already understand or run the project.
- Put contributing, credits, and license near the end.

## What to borrow from excellent READMEs

When a reference README is especially strong, study the underlying choices rather than copying its wording.

Good patterns to reuse:

- A clear one- or two-sentence value proposition near the top.
- Language-switcher links near the top when the repository intentionally ships translated README files.
- A fast path to first success with copy-pasteable commands.
- Concrete examples that show what the project looks or feels like in practice.
- Visual proof placed where it resolves uncertainty fastest, such as a screenshot after the opening summary or a short demo near usage.
- Carefully placed notes or tips to warn about common mistakes.
- Deeper sections that expand only after the reader already understands the basics.
- Real proof such as screenshots, sample output, demo links, or example repositories when available.

## Visual asset guidance

When reviewing or drafting a README, actively evaluate whether an image, GIF, video, or sample-output block would materially improve comprehension or trust.

Do not treat visuals as decoration. Recommend them only when they help the reader understand one of these things faster:

- what the product looks like
- what the workflow feels like
- what success looks like
- what a key interaction or result produces

Detect likely visual insertion points by looking for sections that would otherwise force the reader to imagine the result:

- immediately below the title or About section for apps, websites, and polished user-facing tools
- after Features when a gallery or comparison image would make benefits concrete
- near Getting Started when the user needs to recognize a successful install, build, or run state
- inside Usage when a workflow has multiple UI states or meaningful transitions
- near CLI examples when a sample output block or terminal recording would clarify behavior better than prose
- near Architecture or Project Structure only when a diagram would simplify a concept that text is making heavy

Choose the asset type intentionally:

- Use a static image when one screen, state, or artifact is enough.
- Use a GIF only for short loops that demonstrate interaction or animation more clearly than stills.
- Use a video when the flow is longer, includes audio, or would become too large or distracting as a GIF.
- Use sample output instead of media for CLIs, generators, and tooling when the result is primarily textual.

When assets already exist in the repository, inspect them and place them where they support the reader best.

When assets do not exist, do not invent filenames or links. Instead, explicitly recommend:

- where the visual should appear in the README
- what it should show
- why that placement helps
- which format is most appropriate: image, GIF, video, or sample output

Example recommendation style:

- Add a product screenshot immediately below `## About` to show the default dashboard state before the feature list.
- Add a short GIF in `## Usage` that shows the create-edit-save flow because the value is in the transition, not the final screen.
- Add a terminal output example after the install command so readers can confirm the tool launched successfully.

## Repo-type guidance

### Apps and products

Prioritize product positioning, major user-facing features, platform requirements, setup, and project structure.

Common sections:

- About
- Features
- Tech Stack
- Architecture or Project Structure
- Requirements
- Getting Started
- Support or Author

If screenshots, App Store links, demo videos, or sample data exist, include them where they strengthen trust.

For user-facing apps, actively check whether the README should show the product near the top rather than waiting until later sections.

### Libraries, frameworks, SDKs, and CLIs

Prioritize installation, first-run success, usage, API entry points, compatibility, and examples.

Common sections:

- About
- Getting Started or Installation
- Usage
- Examples or See It In Action
- Project Structure or Concepts
- Requirements or Compatibility
- Contributing
- License

For these repos, a runnable quick start is usually more important than an exhaustive feature list.

For CLIs and developer tools, prefer sample output first. Recommend GIFs or videos only when interaction, progress, or UI state changes are central to understanding the tool.

### Internal tools and utilities

Prioritize purpose, inputs and outputs, workflow, commands, environment assumptions, and operational notes.

Common sections:

- About
- What it does
- Requirements
- Setup
- Usage
- Operational notes

## Multilingual README support

Only use this when the user explicitly asks for multilingual support, translated READMEs, or localized README structure.

Default behavior:

- Keep one primary `README.md` unless the repo already ships translated docs or the user asks to add them.
- If translated READMEs already exist, preserve or improve the language switcher near the top of the primary README.
- Prefer a compact language switcher line such as:
  `[English](README.md) | [Italiano](Docs/README.it.md)`
- Keep the primary README authoritative. Translated files should mirror the same structure and claims.
- Do not invent translations the user did not ask for.
- Do not claim multi-language documentation support unless the translated files actually exist or you are creating them in this task.

When creating or updating multilingual READMEs:

1. Inspect existing translated files and naming patterns such as `Docs/README.it.md`.
2. Keep section ordering consistent across languages.
3. Preserve product names, API names, code blocks, commands, and identifiers in their original form unless translation would be incorrect.
4. Translate interface copy and explanatory prose, not code.
5. If you cannot verify all translations, say so and limit changes to the languages requested by the user.

Borrow from strong multilingual READMEs:

- Put the language switcher immediately below the title.
- Keep it short and scannable.
- Link only to files that actually exist after your changes.

## License handling

License sections must match the repository’s actual license state or the user’s explicit instruction.

Rules:

- If the repository already has a license file, match it.
- If the user explicitly asks for MIT license support, you may add or improve a README license section that points to `LICENSE`, but do not imply the repo is MIT-licensed unless that is already true or you are also creating/updating the license file as part of the task.
- Prefer a short license section such as:
  `## License`
  `[MIT](LICENSE)`
- For proprietary or unknown licensing, do not replace it with MIT wording unless the user explicitly wants that change.
- If the user asks for MIT support and no `LICENSE` file exists, note that the README change alone is incomplete and the repository should also include the MIT license text.

## Rewrite workflow

When rewriting an existing README:

1. Preserve factual content that is still correct.
2. Remove stale, vague, duplicated, or generic text.
3. Reorganize sections for scanability and momentum.
4. Tighten the copy so it sounds intentional rather than templated.
5. Keep the final README consistent with the repository's real state.
6. Check whether any section would be materially clearer with a visual or sample-output recommendation, and add that recommendation when appropriate.

## Inspiration workflow

If the user provides another README as inspiration:

1. Copy the useful structure, pacing, and level of polish.
2. Adapt the sections to the target repository instead of copying blindly.
3. Keep the target project's identity, terminology, and facts.
4. Re-check every claim against the actual codebase.
5. If the inspiration README includes multilingual navigation or a particularly clean license section, borrow the pattern only when it fits the target repo and has factual support.
6. Name the borrowed patterns explicitly in your head: quick start, proof, examples, warnings, structure, tone, multilingual navigation, license presentation.

## Quality rules

- Never invent features or technical details.
- Never invent translated docs, supported languages, or license terms.
- Never invent screenshots, GIFs, videos, filenames, or hosted demo links that do not exist.
- Prefer concrete language over generic marketing copy.
- Keep onboarding steps executable and minimal.
- Use fenced code blocks for commands or example usage.
- Match depth to the size and maturity of the repo.
- Prefer clean markdown and predictable section order.
- Keep lists readable; avoid turning the README into a dump of implementation trivia.
- If the repository is sparse, write a concise README instead of fabricating completeness.
- If setup steps are uncertain, say only what is verified from the project files.
- Include notes, tips, warnings, screenshots, GIFs, videos, demo links, or sample output only when they add real clarity.

## Signals to inspect before writing

Inspect only what is useful:

- `README.md`
- translated README files such as `Docs/README.*.md`, if present or requested
- `LICENSE`, `LICENSE.md`, or equivalent license files
- project manifests such as `Package.swift`, `*.xcodeproj`, `*.xcworkspace`, `package.json`, `pyproject.toml`, `Cargo.toml`
- app entry points and main modules
- source tree layout
- tests
- docs folder
- assets, screenshots, or sample output
- example apps, starter templates, or sample repositories
- existing demo videos or screen recordings

## Output standard

The finished README should be:

- accurate
- specific to the repo
- easy to scan
- polished but not over-written
- stronger than a boilerplate template
- useful to a first-time reader within the first screenful

If visuals would materially improve the README and no assets are present, the output may include a short, explicit recommendation in the relevant section or in a concise follow-up note.
