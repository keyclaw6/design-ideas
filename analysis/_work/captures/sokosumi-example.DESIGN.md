---
version: alpha
name: Example Domain
description: >-
  A minimal, documentation-focused design system emphasizing clarity and functional simplicity. Built for reference
  implementations with restrained color and typography.
logo:
  src: data:,
colors:
  surface: '#eeeeee'
  surface-dim: '#e0e0e0'
  surface-bright: '#f5f5f5'
  surface-container-lowest: '#f9f9f9'
  surface-container-low: '#f0f0f0'
  surface-container: '#eeeeee'
  surface-container-high: '#e9ecef'
  surface-container-highest: '#e0e0e0'
  on-surface: '#000000'
  on-surface-variant: '#505050'
  inverse-surface: '#1a1a1a'
  inverse-on-surface: '#f5f5f5'
  outline: '#d0d0d0'
  outline-variant: '#b0b0b0'
  surface-tint: '#334488'
  primary: '#334488'
  on-primary: '#ffffff'
  primary-container: '#e8ecf5'
  on-primary-container: '#1a2d4d'
  inverse-primary: '#7fa3d1'
  secondary: '#6c757d'
  on-secondary: '#ffffff'
  secondary-container: '#e9ecef'
  on-secondary-container: '#2d3f4f'
  tertiary: '#f0f9fa'
  on-tertiary: '#0a3d47'
  tertiary-container: '#b3e5fc'
  on-tertiary-container: '#001f26'
  error: '#d32f2f'
  on-error: '#ffffff'
  error-container: '#ffebee'
  on-error-container: '#b71c1c'
  primary-fixed: '#e8ecf5'
  primary-fixed-dim: '#c9d5e8'
  on-primary-fixed: '#0d1a2d'
  on-primary-fixed-variant: '#1a2d4d'
  secondary-fixed: '#e9ecef'
  secondary-fixed-dim: '#cdd2d8'
  on-secondary-fixed: '#1a2530'
  on-secondary-fixed-variant: '#3d4f5f'
  tertiary-fixed: '#b3e5fc'
  tertiary-fixed-dim: '#80deea'
  on-tertiary-fixed: '#001f26'
  on-tertiary-fixed-variant: '#00474f'
  background: '#eeeeee'
  on-background: '#000000'
  surface-variant: '#d0d0d0'
typography:
  display:
    fontFamily: system-ui, -apple-system, sans-serif
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
    letterSpacing: '-0.02em'
  headline-lg:
    fontFamily: system-ui, -apple-system, sans-serif
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 40px
    letterSpacing: '-0.01em'
  headline-md:
    fontFamily: system-ui, -apple-system, sans-serif
    fontSize: 24px
    fontWeight: '700'
    lineHeight: 32px
    letterSpacing: 0em
  title-lg:
    fontFamily: system-ui, -apple-system, sans-serif
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
    letterSpacing: 0.01em
  body-lg:
    fontFamily: system-ui, -apple-system, sans-serif
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
    letterSpacing: 0em
  body-md:
    fontFamily: system-ui, -apple-system, sans-serif
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
    letterSpacing: 0em
  label-md:
    fontFamily: system-ui, -apple-system, sans-serif
    fontSize: 14px
    fontWeight: '600'
    lineHeight: 20px
    letterSpacing: 0.02em
  label-sm:
    fontFamily: system-ui, -apple-system, sans-serif
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
    letterSpacing: 0.03em
rounded:
  sm: 2px
  DEFAULT: 4px
  md: 6px
  lg: 8px
  xl: 12px
  full: 9999px
spacing:
  unit: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 32px
  gutter: 16px
  container-max: 960px
elevation:
  sm: 0 1px 3px rgba(0, 0, 0, 0.08)
  md: 0 3px 8px rgba(0, 0, 0, 0.15)
  lg: 0 8px 16px rgba(0, 0, 0, 0.12)
layout:
  containerMaxWidth: 960px
  gridColumns: 12
components:
  button-primary:
    backgroundColor: '{colors.primary}'
    textColor: '{colors.on-primary}'
    typography: '{typography.label-md}'
    rounded: '{rounded.DEFAULT}'
    padding: 8px 16px
    height: 40px
    border: none
    cursor: pointer
  button-primary-hover:
    backgroundColor: '#2a3a6f'
    textColor: '{colors.on-primary}'
    transition: background-color 150ms ease-in-out
  button-primary-active:
    backgroundColor: '#1f2a52'
    textColor: '{colors.on-primary}'
  button-secondary:
    backgroundColor: transparent
    textColor: '{colors.primary}'
    typography: '{typography.label-md}'
    rounded: '{rounded.DEFAULT}'
    padding: 8px 16px
    height: 40px
    border: 1px solid {colors.outline}
    cursor: pointer
  button-secondary-hover:
    backgroundColor: '{colors.surface-container-high}'
    textColor: '{colors.primary}'
    transition: background-color 150ms ease-in-out
  link:
    textColor: '{colors.primary}'
    textDecoration: underline
    typography: '{typography.body-md}'
    cursor: pointer
  link-hover:
    textColor: '#2a3a6f'
    transition: color 150ms ease-in-out
  select-dropdown:
    backgroundColor: '#ffffff'
    textColor: '{colors.on-surface}'
    typography: '{typography.body-md}'
    rounded: '{rounded.DEFAULT}'
    border: 1px solid {colors.outline}
    padding: 6px 12px
    boxShadow: '{elevation.md}'
  select-option:
    backgroundColor: transparent
    textColor: '{colors.on-surface}'
    padding: 6px 12px
    lineHeight: '1.5'
  select-option-hover:
    backgroundColor: '{colors.tertiary}'
    textColor: '{colors.on-surface}'
    cursor: pointer
  select-option-selected:
    backgroundColor: '{colors.surface-container-high}'
    textColor: '{colors.on-surface}'
  select-disabled:
    backgroundColor: '{colors.surface-container-high}'
    textColor: '{colors.on-surface-variant}'
    borderColor: '{colors.on-surface-variant}'
    cursor: not-allowed
    opacity: '0.6'
  card:
    backgroundColor: '{colors.surface-container}'
    rounded: '{rounded.lg}'
    padding: '{spacing.lg}'
    boxShadow: '{elevation.sm}'
    border: 1px solid {colors.outline}
  card-hover:
    backgroundColor: '{colors.surface-container-high}'
    boxShadow: '{elevation.md}'
    transition: all 200ms ease-in-out
---

## Overview

Example Domain is a reference implementation design system built for documentation and educational contexts. It serves developers, technical writers, and educators who need a clear, unambiguous interface for demonstrating web concepts without distraction. The aesthetic is 'Functional Minimalism'—a deliberate rejection of trend-driven design in favor of clarity, accessibility, and timeless simplicity. The UI evokes trust and precision: neutral grays (#eeeeee, #e9ecef) provide a calm canvas, while a restrained blue accent (#334488) signals interactivity without visual noise. Users encounter a page that feels like a well-organized textbook: organized, legible, and focused on content over decoration.

The brand voice is direct, instructional, and free of marketing language. Vocabulary favors clarity over cleverness: 'Learn more' instead of 'Discover,' 'Avoid use in operations' instead of 'Not production-ready.' Tone is neutral and authoritative, as befits a reference. Example sentence in brand voice: 'This domain is reserved for documentation examples—use it freely in your tutorials without requesting permission.'

## Colors

The color palette is deliberately restrained, built on a neutral foundation with a single accent. Surface colors (#eeeeee, #e9ecef, #e0e0e0) form a subtle hierarchy for containers and interactive states, while on-surface text (#000000) ensures maximum legibility. The primary accent is a muted blue (#334488), used exclusively for interactive elements—links, buttons, and focus states. This color is chosen for its professional connotation and sufficient contrast (WCAG AA) against both light and dark backgrounds. Secondary grays (#6c757d, #505050) support disabled states and secondary text. The tertiary color (#f0f9fa, a pale cyan) is reserved for hover states in dropdowns and selection highlights, providing visual feedback without overwhelming the interface. Error states use a standard red (#

## Typography

The type system uses a single font family—system-ui, -apple-system, sans-serif—to ensure consistent rendering across all platforms and eliminate font-loading delays. This choice reinforces the 'reference implementation' aesthetic: the system is about content and clarity, not typographic flourish. Display (48px, 700 weight) is reserved for page titles; headline-lg (32px, 700) for section headers; headline-md (24px, 700) for subsections; body-md (16px, 400) for body copy and form labels; label-md (14px, 600) for button text and UI labels. Line-height is set to 1.5 for body text (24px on 16px base) to ensure readability in dense documentation contexts. Letter-spacing is minimal (0em to 0.03em) to maintain a compact, professional appearance. On small labels over busy backgrounds (e.g., disable

## Layout

The layout uses a fixed-width container (960px max-width, centered with 60vw width on the hero) to maintain focus and readability. The 12-column grid system provides flexibility for future expansion while keeping the current single-column hero layout clean. Spacing follows a 4px unit system: sm (8px) for tight grouping, md (16px) for standard padding and margins, lg (24px) for section separation. The hero section uses 15vh vertical margin (approximately 120px on a 800px viewport) to create breathing room above the title. Body text is set to 80% opacity (opacity: 0.8 on the container div) to create visual hierarchy without changing color values. Gutter spacing is 16px, applied consistently to card padding and form field margins. Container max-width of 960px ensures that even on ultra-wide d

## Elevation & Depth

Elevation is conveyed through subtle shadows and background color shifts rather than dramatic depth. Level 1 (Base): the page background is #eeeeee with no shadow. Level 2 (Standard Cards & Dropdowns): box-shadow: 0 3px 8px rgba(0, 0, 0, 0.15), background: #ffffff or #f9f9f9, border: 1px solid #d0d0d0. Level 3 (Hover/Active States): box-shadow: 0 8px 16px rgba(0, 0, 0, 0.12), background: #e9ecef. The dropdown panel uses the Level 2 shadow (0 3px 8px rgba(0, 0, 0, 0.15)) and sits 4px below the trigger button (margin-top: 4px). Hover states on interactive elements transition smoothly (150ms ease

## Shapes

The shape philosophy is 'Technical Precision'—minimal rounding that signals interactivity without softness. Buttons and form controls use 4px border-radius (rounded.DEFAULT), a subtle curve that distinguishes them from sharp edges while maintaining a professional, engineered appearance. Cards and dropdown panels use 8px border-radius (rounded.lg) to create slightly more breathing room for larger containers. Disabled states and secondary surfaces use 6px border-radius (rounded.md) as a middle ground. The select dropdown arrow is created with pure CSS (border-left/right/top technique) rather tha

## Components

### Action Elements
Buttons use a 40px height with 8px vertical and 16px horizontal padding (padding: 8px 16px). Primary buttons (#334488 background, white text) transition to #2a3a6f on hover (150ms ease-in-out) and #1f2a52 on active/click. Secondary buttons have a transparent background with a 1px solid #d0d0d0 border, transitioning to #e9ecef background on hover. Links are underlined and use the primary color (#334488), transitioning to #2a3a6f on hover. All interactive elements include cursor: pointer; disabled states set cursor: not-allowed and reduce opacity to 60%.

### Containers & Surfaces
Cards use a background of #eeeeee (surface-container) with 16px padding (md spacing), a 1px solid #d0d0d0 border, and box-shadow: 0 3px 8px rgba(0, 0, 0, 0.15). On hover, the background shifts t

## Do's and Don'ts

**Do**
- Do use the primary blue (#334488) exclusively for interactive elements—links, buttons, focus states—to create a consistent affordance language.
- Do maintain 16px (md spacing) as the default padding and margin unit; use sm (8px) only for tight groupings within components.
- Do apply the 150ms ease-in-out transition to all hover and active state changes on buttons and links to signal interactivity smoothly.
- Do keep text at 100% opacity on the body and use the surface-container colors (#e9ecef, #e0e0e0) to create visual hierarchy rather than opacity shifts.
- Do use system-ui font stack exclusively; do not introduce custom web fonts, which would contradict the reference-implementation aesthetic.

**Don't**
- Don't use the primary color (#334488) for backgrounds, body text, or non-interactive elements; reserve it for CTAs and focus states only.
- Don't apply border-radius greater than 8px (rounded.lg) to any component; pill-shaped buttons and fully rounded corners violate the Technical Precision aesthetic.
- Don't add drop shadows greater than 0 8px 16px rgba(0, 0, 0, 0.12); excessive shadow depth contradicts the minimal, reference-focused design.
- Don't introduce new accent colors or gradients; the palette is intentionally limited to surface grays, primary blue, and tertiary cyan for consistency.
- Don't animate or transition opacity on interactive elements; use background-color and box-shadow transitions only to maintain clarity and predictability.
