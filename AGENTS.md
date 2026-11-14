# AGENTS.md

Instructions for AI coding agents (Claude Code, Codex, Cursor, etc.) working in this repo. Works like CLAUDE.md.

## Project phases
Always ask which phase the owner is in before suggesting code.
1. Phase 1: Django full-stack site in `backend/` (templates, admin)
2. Phase 2: JSON API added to `backend/` with Django REST Framework
3. Phase 3: Next.js frontend in `frontend/` consuming the API; Django admin stays the CMS
Do not start a later phase early, and do not remove Phase 1 code until Phase 3 is deployed and working.

## Project
Django portfolio for Tarun Suthar with two personalities behind a split landing page:
Creative (`/creative/`) and Technical (`/technical/`). Read `DESIGN.md` for visuals, `FEATURES.md` for scope, `INITIALSETUP.md` for setup.

## Owner context (important)
The owner is learning Django by building this. So:
- Work in small steps. One concept per change.
- Explain what each new file or line does in plain words, briefly, and why Django does it this way.
- Prefer the simplest approach that works. No extra libraries without asking.
- Don't rewrite large areas at once. Ask before restructuring.
- When the owner asks "how", teach first. Write the full solution only if asked.

## Stack
Backend (`backend/`): see below. Frontend (`frontend/`, Phase 3): Next.js App Router, TypeScript, CSS Modules (no Tailwind), Framer Motion, `next/font`, `next/image`.
- Python 3.11+, Django 5.2 LTS (check before upgrading), SQLite in dev
- Apps: `core`, `creative`, `technical`
- Plain HTML templates, plain CSS, vanilla JS. No frontend framework, no Tailwind, no build step.
- Pillow for images, WhiteNoise for static files, python-dotenv for settings

## Commands
```bash
source .venv/bin/activate          # Windows: .venv\Scripts\activate
python manage.py runserver
python manage.py makemigrations && python manage.py migrate
python manage.py createsuperuser
python manage.py test
python manage.py collectstatic
```

## Frontend commands (Phase 3)
```bash
cd frontend
npm install
npm run dev        # http://localhost:3000
npm run lint && npm run build
```

## API contract rules
- Endpoints are read-only GET. Do not add public write endpoints without asking.
- Changing a serializer field means updating `frontend/src/lib/types.ts` in the same change.
- Never put secrets in `NEXT_PUBLIC_*` variables.
- Image URLs from the API are absolute. Allow the host in `next.config.ts`.

## Frontend rules (Phase 3)
- Server components fetch data; client components only for interaction (drag, canvas, lightbox)
- Port behaviour from the existing vanilla JS exactly (thresholds, easing), as described in `DESIGN.md`
- Gestures go in custom hooks (`useSplitDrag`), canvas in `useEffect` with cleanup
- Check `useReducedMotion` for every animation

## Structure rules
- Templates in `templates/`, extend `base.html`
- CSS per page in `static/css/`, JS per page in `static/js/`. No inline `<style>` or `<script>` except tiny snippets.
- Content comes from models via views. Never hard-code portfolio text in templates once the model exists.
- Keep views thin. Put data helpers on models (see `skill_list`, `tech_list`).
- Secrets only in `.env`. Never commit `.env`, `db.sqlite3`, `media/`.

## Design rules (summary, full detail in DESIGN.md)
- Creative: royal blue `#1820EF`, cream `#FAFAED`, yellow `#FFC524`, cherry `#FF4E42`, burgundy `#832626`. Fonts: Inter Tight, Playfair Display italic, M PLUS Rounded 1c.
- Technical: deep `#0c141c`, mint `#87BC87`, teal `#73B3C5`. Fonts: Michroma, Space Mono. CRT scanlines, digit field.
- The two sides must look like two different brands. Never mix their fonts or palettes.
- The landing gateway uses a text wordmark only; do not add a round face logo there.
- Do not render the illustrated full-body character on the landing, Creative, or Technical pages.
- Respect `prefers-reduced-motion`, keep keyboard access and visible focus.

## Code style
- Python: PEP 8, 4 spaces, small functions, docstring when not obvious
- Django: class names singular, `verbose_name_plural` where needed, order fields via `Meta.ordering`
- JS: `const`/`let`, no globals beyond one object per file, comment the why
- Mobile first, breakpoint at 800px

## Definition of done for a change
1. `python manage.py check` passes, migrations created if models changed
2. Page loads without console errors on desktop and a narrow mobile viewport
3. Gestures still work: seam drag (desktop), swipe (mobile), Esc and back navigation
4. In Phase 3: `npm run lint` and `npm run build` pass, and TypeScript has no errors
5. No new dependency without a note in `requirements.txt` and a reason in the PR or commit message

## Do not
- Do not delete or reset the database or migrations without asking
- Do not invent personal facts (grades, links, employers). Use admin data or ask.
- Do not add trackers, ads or third-party scripts
- Do not run destructive git commands
