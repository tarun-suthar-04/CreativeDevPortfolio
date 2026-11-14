# FEATURES.md

Status key: [P] describes the intended/reference prototype behavior, [D] planned for Django (Phase 1), [A] planned for API (Phase 2), [N] planned for Next.js (Phase 3), [+] optional later. The prototype source is not present in the current repository, so [P] is not a claim that the code exists here.

Every [P][D] UI feature below is rebuilt as [N] in Phase 3 with the same behaviour.

## Landing (`/`)
- [P][D] 50/50 vertical split: Creative left, Technical right
- [P][D] Hover widens a half (flex-grow 1.35, 0.7s)
- [P][D] Click opens a half (in Django: animate, then go to the route)
- [D] Text wordmark in the top bar; no round face logo or illustrated character on the landing page
- [P][D] Desktop: hold the seam and drag left for Technical, right for Creative, with live resize, threshold, flick and spring-back
- [P][D] Mobile: halves stack, swipe up for Technical, swipe down for Creative
- [P][D] Hint labels, grip line, keyboard (arrows on seam, Enter on a half)
- [P][D] Top bar: name and location
- [P][D] Creative half: staggered mixed type headline, pill CTA, chips, tilted cards, cursor glow, wave pattern
- [P][D] Technical half: Severance headline, frame with progress bar, bins, digit canvas, scanlines

## Creative page (`/creative/`)
- [P][D] Sticky nav with tabs: Featured, Personal, Stories, About, Back
- [P][D] Auto-scrolling strips of work tiles, alternating directions, pause on hover
- [P][D] Tab filtering by category (JS, or `?cat=` query in a view)
- [P][D] Lightbox for a tile
- [D] About: statement, focus list, and stats; no illustrated character portrait
- [P][D] Contact footer (email, Fiverr, LinkedIn, GitHub)
- [D] Works managed in admin (image, category, colour, aspect ratio, order)
- [+] Individual work detail page, `/creative/<id>/`
- [+] Video support for Stories

## Technical page (`/technical/`)
- [P][D] Sticky nav with section jump buttons
- [D] Record header: stamp and bio; no illustrated character portrait
- [P][D] Skills in three groups
- [P][D] Projects with bullets and tech chips
- [P][D] Education table, certifications, achievements, currently learning
- [P][D] Contact links
- [D] All content from admin models
- [+] Project detail pages with screenshots
- [+] Download CV button (FileField in SiteSettings)

## API (Phase 2)
- [A] Read-only JSON: `/api/site/`, `/api/works/?category=`, `/api/technical/`
- [A] Absolute image URLs, CORS limited to the frontend origin
- [A] Tests for each endpoint
- [+] Pagination for works, caching headers

## Next.js frontend (Phase 3)
- [N] Same landing, drag, swipe, strips, digit field and pages
- [N] Smooth expand-to-page transition without a reload (Framer Motion)
- [N] Server-rendered pages with `revalidate` so admin edits appear within about a minute
- [N] `next/image` for work images, `next/font` for fonts
- [N] Typed API client (`lib/api.ts`, `lib/types.ts`)
- [+] Intercepting routes or View Transitions for shared-element feel
- [+] Contact form posting to a Django endpoint

## Cross-cutting
- [D] Django admin for all content, site settings singleton
- [D] Static files and media uploads
- [D] `prefers-reduced-motion` respected
- [D] Responsive, safe-area insets
- [D] SEO basics: titles, meta description, Open Graph image
- [+] Contact form (Django form plus email backend)
- [+] Sitemap and robots.txt
- [+] HTMX for in-page transitions that mimic the prototype overlay
- [+] Tests for views and models
- [+] Analytics (privacy friendly)

## Definition of done (v1)
- v1 (Phase 1): Django site with landing, both pages, admin content, drag and swipe, deployed
- v2 (Phases 2–3): API live, Next.js frontend on Vercel reading it, Django admin as the dashboard, same visuals and gestures as v1
