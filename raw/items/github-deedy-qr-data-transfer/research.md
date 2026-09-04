# Research

## What it is

QRFerry: a TypeScript, fully client-side file transfer that streams a file as an animated QR code from a laptop to a phone camera — nothing is uploaded to a server.

## How it works

- Sender opens the root page and picks a file; receiver opens `/scan` and allows camera.
- Payload is compressed (Brotli/gzip) then encoded as raw-byte QR frames using RaptorQ fountain codes (RFC 6330) in WebAssembly so frames can arrive out of order.
- Turbo profiles at 15/30/60 fps; dual-lane V30-L for more stable high-speed transfer.
- Rendering via fast_qr WASM; scanning via ZXing-C++ WASM; save when recovery hits 100%.
- Dev: `npm install && npm run dev`, Node ≥ 22.13. No backend.

## Why saved

Unusual UX pattern: air-gapped, camera-mediated transfer with fountain codes. Useful as a craft reference for offline/kiosk/field tools and as a “no server, still delightful” interaction — not a BESS flythrough, but a complete productized demo.

## Topics

`design`

## Related

`web-dicebear`, `web-tinyshots`, `web-checklist-design`, `github-nateherkai-scroll-craft`, `web-animos-editor`

## Use when

Designing camera-to-desktop or air-gapped handoff UX; looking for fountain-code / animated-QR precedents; shipping a browser-only utility that should feel like a product, not a lab demo.
