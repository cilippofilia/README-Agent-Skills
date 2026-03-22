# Special Cases

Use this reference for multilingual README work and license-sensitive README sections.

## Multilingual README support

Use only when the user explicitly asks for multilingual support or when translated README files already exist.

Rules:

- Keep one primary `README.md` unless the repo already ships translated docs or the user asks to add them.
- Preserve or improve the language switcher near the top of the primary README.
- Keep the primary README authoritative.
- Keep section ordering and claims aligned across languages.
- Do not invent translated files or languages the repo does not support.

Recommended switcher style:

`[English](README.md) | [Italiano](Docs/README.it.md)`

## License handling

License sections must match the repository's actual license state or the user's explicit instruction.

Rules:

- If a license file exists, match it.
- If the user wants a README license section, point to the real file.
- Do not imply MIT or any other license unless it is already true or is being added in the same task.
- For unknown or proprietary licensing, avoid replacing it with generic open source wording.

Recommended minimal style:

`## License`
`[MIT](LICENSE)`

## Common mistakes

- claiming multilingual support when translated files do not exist
- linking to translated README paths that are not present
- rewriting the license section to a different license than the repo actually uses
