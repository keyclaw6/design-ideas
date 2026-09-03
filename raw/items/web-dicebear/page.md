# DiceBear

**Landing:** https://www.dicebear.com  
**Playground:** https://www.dicebear.com/playground/  
**HTTP API:** `https://api.dicebear.com/10.x/{style}/{format}?seed={seed}`

> Privacy-focused, open source avatar library with 61 avatar styles. Deterministic profile pictures via API and multi-language libraries.

## Delivery options

- HTTP API
- JavaScript (`@dicebear/core` + style packages)
- PHP, Python, Rust, Go, Dart, C# libraries
- CLI: `npx dicebear lorelei --seed 'Felix'`

## Example (Lorelei style)

```
https://api.dicebear.com/10.x/lorelei/svg?seed=Felix
```

## Use cases (site)

| Use case | Value |
|----------|-------|
| User profiles | Unique avatar from day one — no upload, no Gravatar fallback |
| Chat apps | Deterministic from user ID; consistent across devices |
| Gaming | Millions of player/NPC identities from seeds |
| Forums | Distinct identities for community trust |
| Team tools | Consistent faces in cursors, mentions, sidebars |
| Placeholders | Defaults while account setup pending |

## Avatar maker (no code)

Visual editor at https://editor.dicebear.com/ — customize hair, eyes, accessories; export PNG.

## Custom styles (Figma workflow)

1. Design components in Figma with DiceBear naming conventions
2. Export via DiceBear Studio Figma plugin
3. Single JSON definition consumed by all DiceBear libraries

## License

Core library MIT licensed; open development on GitHub.
