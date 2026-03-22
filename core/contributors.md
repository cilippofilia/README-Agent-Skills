# Contributors

Use this reference when deciding whether to add `Contributing` and `Contributors` sections to a README.

## When to add them

Add a `Contributing` section when:

- the repository is intended to be improved over time
- outside contributors or teammates would benefit from direction
- the repo has multiple files or topic areas and contribution targets are not obvious

Add a `Contributors` section when:

- contributor names can be verified from git history, an existing section, or user-provided information
- a short attribution list adds value for readers or maintainers
- git identity or hosting metadata is available to render contributor name and avatar accurately

## What `Contributing` should cover

A good `Contributing` section should answer:

- what kinds of changes are useful
- where contributors should make those changes
- why those contributions matter

Keep it practical. Prefer concrete contribution targets over generic “PRs welcome” wording.

## What `Contributors` should cover

- place it near the bottom of the README
- keep it short and factual
- list only verified names
- prefer git-derived identity over manually typed names when available
- prefer verified avatars from the repository host or the contributor profile when available
- do not invent handles, roles, links, affiliations, or avatar URLs

## Preferred data sources

When building a contributor entry, use the strongest verified source available:

1. `git shortlog -sne HEAD` or `git log` for contributor names and emails
2. `git config user.name` and `git config user.email` for the local primary author when that matches the repository's intended contributor display
3. `git remote -v` to detect the repository host and owner namespace
4. existing profile links in the README or repository metadata, if present

## Avatar guidance

- If the repo is hosted on GitHub and the contributor maps cleanly to a GitHub profile, prefer the GitHub avatar image.
- If a contributor image cannot be verified confidently, fall back to a text-only contributor entry.
- Do not guess avatar URLs from unverified usernames.

## Recommended rendering

For a single primary contributor, prefer a compact card or linked avatar plus name.

Example pattern:

```html
<a href="https://github.com/example-user">
  <img src="https://github.com/example-user.png" width="72" alt="Example User" />
</a>
```

- Example User

## Example pattern

`## Contributing`

- improve routing logic in `SKILL.md`
- refine topic guidance in `core/`
- tighten examples and reduce unsupported claims

`## Contributors`

- Verified Person Name
