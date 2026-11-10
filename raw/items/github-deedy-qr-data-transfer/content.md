# QRFerry (qr-data-transfer)

> Source: https://github.com/deedy/qr-data-transfer — by deedy — captured 2026-09-02T17:15:19Z — stats-at-capture: stars=460; forks=87; language=TypeScript

## Article

**Repo:** deedy/qr-data-transfer  
**Stars:** 460 · **Language:** TypeScript

Browser-only file transfer via animated QR stream. Sender and receiver run entirely client-side; file never uploaded to a server.

## Usage

1. Open root page on sender, choose file
2. Open `/scan` on receiver phone, allow camera
3. Start QR stream; save when RaptorQ recovery hits 100%

## Protocol highlights

- Brotli/gzip compression; raw byte mode QR frames
- RaptorQ fountain codes (RFC 6330) in WebAssembly
- Turbo profiles: 15/30/60 fps; dual-lane V30-L for stable high-speed transfer
- Rendering: fast_qr WASM; scanning: ZXing-C++ WASM

## Dev

```bash
npm install && npm run dev
```

Requires Node.js ≥ 22.13.0.
