# Header Composition

Use this reference for the top block of a README: hero images, logos, support badges, contact badges, and hidden improvement comments.

## Goal

Make the first screenful answer four questions quickly:

1. what is this project?
2. what does it run on?
3. who maintains it?
4. what proof or polish is still missing?

## Recommended top-of-README order

When the assets and metadata are available, prefer this order:

1. centered logo or hero image block
2. compact support badges
3. optional verified contact badge
4. `# Title`
5. one-sentence value proposition

Skip any element that cannot be verified. Do not force a visual header for every repo.

## Hero images and logos

- Place a logo, pill, or brand image on its own line above the `# Title`.
- Do not put images inline inside the H1 unless the user explicitly asks for that layout.
- Prefer a centered image block when the repo already has a polished visual asset that improves recognition or trust.
- For low-visual packages and tools, skip the hero image unless it carries real brand or product value.

## Support badges

Support badges are default metadata, not decoration, when the repo explicitly states supported versions.

Use the smallest verified badge set that answers "what does this run on?" immediately.

### Source precedence

When multiple sources exist, use this order:

1. manifest or package declarations such as `Package.swift`
2. Xcode deployment targets and build settings from `.xcodeproj` or `.xcconfig`
3. explicit tested-version metadata such as CI matrices or version config files
4. repo docs only when they are clearly maintained as canonical project metadata

Do not merge competing sources. Use the highest-confidence source available.

If sources disagree:

- omit the conflicting badge
- prefer a hidden improvement comment only if the missing badge materially hurts clarity

Do not infer versions from imports, API usage, or vague prose.

## Contact badges

Add a contact badge only when the maintainer link or handle is explicit and intentional.

Valid sources:

- explicit user input
- existing README metadata
- package metadata
- website or project config that clearly represents the project
- official repository links intended for support or contact

Do not derive contact badges from commit authorship, incidental mentions, or guessed social handles.

## Hidden improvement comments

Use hidden comments only when a missing asset or proof materially hurts clarity or trust.

Syntax:

`[//]: # (comment text)`

Rules:

- place the comment immediately above the affected section
- keep it specific and actionable
- use it selectively, not as routine polish
- prefer comments for missing hero images, screenshots, videos, GIFs, diagrams, or unresolved badge conflicts
- do not use comments for filler, apologies, or generic writing advice
- do not invent filenames or links unless they are clearly labeled as examples

Examples:

- `[//]: # (Hero section: this would benefit from a centered image above the title, for example <p align="center"><img src="Docs/Images/hero.svg" alt="Project logo" width="60%" /></p>)`
- `[//]: # (Usage section: this would benefit from a short demo video or GIF that shows the main workflow end to end.)`
- `[//]: # (Support badges: iOS and macOS versions are not emitted because the manifest and Xcode deployment target disagree.)`
