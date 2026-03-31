# App READMEs

Use this reference for user-facing apps and products.

## Priorities

1. State what the product does and who it is for.
2. Show the product early when visual proof matters.
3. Make major user-facing benefits obvious before technical depth.
4. Document platform requirements and setup accurately.
5. Surface verified platform support near the top when deployment targets or toolchain versions are explicit.

## Recommended section order

- Title
- About
- Visual proof, if available and useful
- Features
- Tech Stack
- Requirements
- Getting Started
- Project Structure or Architecture
- Contributing, if relevant
- Support, Contributors, Author, or License

Do not force every section. Small app repos often need fewer sections.

## What good app READMEs do

- Open with a short value proposition, not a long backstory.
- Use `header.md` when shaping the top block of the README.
- Show the UI near the top when the product experience matters.
- Explain what a new user can do with the app.
- Keep setup steps focused on getting the app running.
- Move architecture below the first-run path.
- Derive Apple platform badges from real deployment targets or manifest metadata when available.

## Visual guidance

For apps, check whether the README should include:

- a centered hero image or logo above the title
- support badges for verified Apple platform or runtime coverage
- a contact badge when the maintainer handle or support URL is verified
- a hero screenshot below `About`
- a small gallery after `Features`
- a short demo GIF in `Usage`
- a video link when the flow is too long or rich for a GIF

Use [header.md](header.md) for the top block and [visual-assets.md](visual-assets.md) for screenshots, GIFs, videos, and placement rules below the header.

## Common mistakes

- Leading with architecture instead of product value
- Listing implementation details as features
- Hiding requirements too far down
- Using visuals as decoration instead of proof
- Inventing screenshots, stores, demos, or supported platforms

## Contributor sections

If the repo is open to community or team updates, include:

- a `Contributing` section that explains what kinds of changes are useful, where to make them, and why they matter
- a `Contributors` section near the bottom when names can be verified from the repo or provided by the user
