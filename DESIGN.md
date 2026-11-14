# DESIGN.md — Tarun Suthar Portfolio

One person, two personalities. A 50/50 split landing page leads into two full
detail pages that look like two different brands. The landing page uses a text wordmark only, with no round face logo or illustrated character.

| | Creative | Technical |
|---|---|---|
| Mood | Funky, editorial, playful | Corporate-sci-fi terminal (Severance / Lumon) |
| Surface | Royal blue, flat, bold | Near-black navy, CRT scanlines |
| Type | Tight grotesque + italic serif + rounded | Wide extended + monospace |
| Motion | Springy, tilting, parallax | Stepped, flickering, digit field |

---

## 1. Brand mark

- Landing gateway: use the text name `Tarun Suthar` in the top bar. Do not place a round face logo or character artwork on the split seam.
- Do not render the illustrated full-body character on the landing, Creative, or Technical pages.
- Avoid a `TS` monogram.

---

## 2. Colour tokens

### Creative (ramen-brand UI kit palette)

| Token | Hex | Use |
|---|---|---|
| `--royal` | `#1820EF` | Page background, button text |
| `--cream` | `#FAFAED` | Text, borders, light tiles |
| `--yellow` | `#FFC524` | Primary accent, CTA, active tab |
| `--cherry` | `#FF4E42` | Secondary accent, hover, glow |
| `--burgundy` | `#832626` | Button hard-shadow, dark tiles |
| `--black` | `#000000` | Work-strip and About background |

### Technical (Lumon-inspired)

| Token | Hex | Use |
|---|---|---|
| `--deep` | `#0c141c` | Background |
| `--mint` | `#87BC87` | Text, borders, digits |
| `--pale-mint` | `#d6efd6` | Headings, primary buttons |
| `--teal` | `#73B3C5` | Secondary text, second headline line |
| `--navy` | `#262C3A` | Reserved surface tone |

Body text on the technical side is `#a9cfae`.

---

## 3. Typography

### Creative
| Role | Font | Spec |
|---|---|---|
| Headline | Inter Tight 700 | `clamp(3.2rem, 9.4vw, 9rem)`, line-height .84, tracking −0.065em |
| Accent word | Playfair Display *italic* 500 | Yellow, tracking −0.04em |
| Staggered body | Inter Tight 500 | `clamp(1.05rem, 1.7vw, 1.45rem)`, line-height 1.02, tracking −0.04em |
| Buttons, chips, labels | M PLUS Rounded 1c 800–900 | Uppercase, tracking .06em |
| Tile and lightbox titles | Playfair Display *italic* | 1.5–1.8rem |

Headlines stack on separate lines with different left indents. The offset is
part of the style.

### Technical
| Role | Font | Spec |
|---|---|---|
| Headline | Michroma 400 | Uppercase, `clamp(1.7rem, 4.2vw, 3.6rem)`, tracking .02em |
| Body, labels, UI | Space Mono 400 | .72–.9rem, line-height 1.7, wide letter-spacing on labels |

Copy voice: dry and corporate ("Please enjoy each project equally").

---

## 4. Layout

### Landing
- Full viewport, two flex halves (`flex: 1 1 0`).
- Hover: hovered half gets `flex-grow: 1.35`, 0.7s `cubic-bezier(.7,0,.2,1)`. Pointer-capable screens ≥ 800px only.
- Click: chosen half `flex-grow: 100`, other `0`. Landing content fades up 30px, detail page fades in.
- Top bar is fixed and fades out when a page is open.
- Content is vertically centred, padded `92px` top and `clamp(24px, 4vw, 64px)` sides.
- Mobile (< 800px): halves stack vertically. Staggered text, tags, cards and bins are hidden.

### Creative landing contents
1. Headline: Ideas / *into* / visuals.
2. Staggered line block
3. Outline chips
4. Yellow pill CTA
5. Three tilted cards, bottom right
6. Wave pattern, yellow wave line, cursor glow behind

### Technical landing contents
1. Bordered frame "TECHNICAL / RECORDS" with progress bar
2. Headline: SYSTEMS / *into tools.*
3. Short description
4. Bins: Projects · Apps · Systems
5. Outline button "Open the file"
6. Canvas digit field, scanlines and vignette behind

### Creative detail page
Sticky blue nav → hero → black auto-scrolling strips → About (two columns) → yellow contact footer.

### Technical detail page
Sticky dark nav → record header (stamp + bio) → Skills → Projects → Education → Credentials → Currently learning → Contact. Do not use the illustrated character as the record portrait. Content max-width 1040px.

---

## 5. Components

### Creative
- **Pill CTA**: yellow fill, royal text, 8px padding with 26px left, full radius. Contains a 38px royal circle with a yellow arrow. `box-shadow: 0 6px 0 burgundy`.
  - Hover: cherry fill, cream text, arrow circle turns cream, arrow slides 5px right.
  - Active: translateY(5px), shadow shrinks to 1px.
- **Chip**: 2px cream outline, full radius, rounded font .8rem. Hover: yellow fill, royal text, tilt −3°.
- **Floating card**: 150×170, radius 26px, Playfair italic 1.5rem, small pill label. Colours: cream/royal, cherry/cream, yellow/royal. Tilts −8°, 5°, −2°. Hover straightens and scales 1.1.
- **Work tile**: radius 22px, aspect ratio from data (3/4, 1/1, 4/5, 16/10), black pill label. Colour variants: blue (with cream border), gradient (cherry → yellow), burgundy, near-black, cream. Hover: scale .96, rotate −1.5°.
- **Tab button**: 2px cream outline pill. Active/hover: yellow fill.
- **Lightbox**: cream card, radius 28px, art, category label, Playfair italic title, royal close pill.
- **Stat card**: 2px cream outline, radius 20px, yellow numeral.

### Technical
- **Frame**: 1px mint border, translucent deep fill, progress bar (37% → 100% on hover, stepped).
- **Bin / chip**: 1px mint border. Hover: mint fill, deep text.
- **Button**: 1px pale-mint outline, uppercase, tracking .18em. Hover: invert.
- **Box**: 1px mint border, 16px padding. Heading has a dashed underline. Hover: 10% mint fill. "Learning" variants use dashed chip borders.
- **Stamp**: mint fill, deep text, .72rem.
- **Table**: mint header row, 1px mint cell borders.

---

## 6. Motion

| Effect | Side | Spec |
|---|---|---|
| Half expand | Both | 0.7s `cubic-bezier(.7,0,.2,1)` |
| Cursor glow | Creative | Lerp .08 toward pointer |
| Headline parallax | Creative | Each line translates by pointer × its own factor (−16 to 26) plus slight rotation |
| Card parallax | Creative | Same, factors −30 / 24 / −14 |
| Springy hover | Creative | `cubic-bezier(.3,1.6,.5,1)` |
| Strips | Creative | Linear marquee 60s+, rows alternate direction, pause on hover |
| Portrait yaw | Creative | ±14° rotateY, 6s ease-in-out |
| Digit field | Technical | Canvas, 44px cells (34px on small screens), drift ±4px, size 11 → 37px within 190px of the pointer, opacity .16 → 1, a few random digit changes every 180ms |
| Scanlines | Technical | 3px repeating lines at 4%, flicker every 6s |

`prefers-reduced-motion: reduce` disables transitions and animations.

---

## 7. Content map

**Creative page**: Featured / Personal / Stories (filter tabs), About, contact (email, Fiverr, LinkedIn, GitHub). Stats: 100+ AI visuals, 30+ videos, ∞ explorations.

**Technical page**: Skills (used / foundational / learning), Projects (Order Analyzer, Pixault, Employee Management System), Education table, Certifications and achievements, Currently learning (Python backend, DevOps & cloud, Security), Contact.

---

## 8. Accessibility and behaviour

- Halves are focusable (`tabindex="0"`, `role="button"`). Enter opens, Esc closes the lightbox first, then the page.
- Visible 2px white focus ring, 3px offset.
- Text sits on solid colour: cream on royal, pale mint on deep.
- Work images use `onerror` fallback to a colour tile, so a failed image never leaves a gap.
- Respects safe-area insets and `prefers-reduced-motion`.

---

## 9. Implementation notes

- Single self-contained HTML file, no build step.
- Fonts (Google Fonts): Inter Tight, Playfair Display, M PLUS Rounded 1c, Michroma, Space Mono. Each needs a fallback stack.
- State is a class on `#stage`: none (split), `oc` (creative open), `ot` (technical open).
- Face logo is embedded as a data URI and reused through `img[data-face]`.
- Remote work images load only where the host allows them. Otherwise tiles show colour placeholders.

---

## 10. Django mapping

| Design element | Where it lives |
|---|---|
| Colour tokens | CSS variables at the top of `static/css/base.css` (creative) and `technical.css` |
| Fonts | `<link>` in `base.html` |
| Split landing | `templates/landing.html`, `static/css/landing.css`, `static/js/landing.js` |
| Landing identity | Text wordmark in the top bar; no round face mark on the landing |
| Work tiles, strips, lightbox | `templates/creative.html`, `static/css/creative.css`, `static/js/creative.js` |
| Digit field | `static/js/digits.js` (canvas) |
| Content | Admin models: Work, SkillGroup, Project, Education, Credential, SiteSettings |

Gesture spec (landing):
- Desktop: pointer down on the seam, track X, `d = dx / (innerWidth/2)` clamped to ±0.8, set creative `flex-grow = 1 + d` and technical `1 - d`, move the seam to `50 + d*50 %`. Commit at |d| ≥ 0.28 or a flick (> 0.6 px/ms and > 50px). Left opens Technical, right opens Creative. Otherwise spring back.
- Mobile (< 800px): same with Y. Threshold 0.2. Up opens Technical, down opens Creative. Stage uses `touch-action: none` while on the landing page only.
- A drag must never trigger the click handler (suppress for about 60ms after release).
- In Django the commit step plays the expand animation (~700ms) then navigates to `/creative/` or `/technical/`.


## 11. Next.js mapping (Phase 3)

| Design element | Where it lives |
|---|---|
| Colour tokens | CSS variables in `app/globals.css`, per-side overrides in CSS modules |
| Fonts | `next/font/google` in `app/layout.tsx` (Inter Tight, Playfair Display, M PLUS Rounded 1c, Michroma, Space Mono) |
| Split landing, seam, hints | `components/SplitLanding.tsx` + `useSplitDrag` hook |
| Open animation | Framer Motion animates the chosen half to full size, then `router.push` |
| Strips, tabs, lightbox | `components/WorkStrips.tsx` (marquee in CSS, filter in state) |
| Digit field | `components/DigitField.tsx` (canvas in `useEffect`, cleanup on unmount, ResizeObserver) |
| Content | Props from server components that fetch the Django API |

Behaviour must match section 10 (gesture spec) exactly: same thresholds, easing and hint labels. With client-side routing the expand animation can run without a reload, so the page transition is smoother than in Phase 1.
