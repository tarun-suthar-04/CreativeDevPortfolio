# CHECKLIST.md — Portfolio build progress

Legend: `[x]` verified complete · `[~]` partial or not confirmed · `[ ]` to do.
Progress below reflects the files, commits, and database checked on 2026-11-21, verified against commits 7697580, 6b5d99d, and f984df2.

---

## Planning and docs
- [ ] Prototype source for the landing, Creative, and Technical pages is not present in this project tree.
- [x] `README.md`, `DESIGN.md`, `FEATURES.md`, `AGENTS.md`, `INITIALSETUP.md`, `CreativeInfo.md`, and `TechnicalInfo.md` are present as documentation and context.
- [x] The current implementation phase is Phase 1 (Django foundation, models, views, and templates in `portfolio/backend/`).

---

## Guided setup — chat 1 (Steps 1–6)

### Step 1: Check tools
- [x] Python 3.11.1 is available in the backend virtual environment
- [x] Git 2.53.0 is available

### Step 2: Folders and virtual environment
- [x] Created `portfolio/backend` and entered it
- [x] `.venv` exists in `portfolio/backend/`
- [~] Activation is session-specific; commands run using `.venv\Scripts\activate` or directly via virtual environment python

### Step 3: Install packages
- [x] Django 5.2.19, Pillow, python-dotenv, WhiteNoise, and Gunicorn are installed and import successfully
- [x] `requirements.txt` is present with pinned dependencies
- [x] Django version command reports 5.2.19

### Step 4: Project and apps
- [x] `django-admin startproject config .`
- [x] Created apps `core`, `creative`, `technical`
- [x] `manage.py` sits directly inside `portfolio/backend/`

### Step 5: First run
- [x] Built-in and `core` migrations are applied
- [x] Django's development server verified functional with `python manage.py check` passing cleanly

### Step 6: Git
- [x] `git init`
- [x] `.gitignore` created (`.venv/`, `__pycache__/`, `db.sqlite3`, `.env`, `media/`, `staticfiles/`)

---

## Guided setup — chat 2 (Steps 7–12)

### Step 7: `.env`
- [x] `.env` has a configured non-default `SECRET_KEY` and `DEBUG=1` (secret kept out of source control)

### Step 8: `config/settings.py`
- [x] 8a: imported `os` and `load_dotenv()`
- [x] 8b: `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS` read from environment
- [x] 8c: added `core`, `creative`, `technical` to `INSTALLED_APPS`
- [x] 8d: WhiteNoise ordered directly after `SecurityMiddleware` (fixed in commit `6b5d99d`)
- [x] 8e: `TEMPLATES['DIRS']` configured and `templates/` directory created with `base.html`, `landing.html`, `creative.html`, `technical.html` (commit `f984df2`)
- [~] 8f: static and media settings are configured; `static/` directory exists (CSS/JS files to be authored)
- [x] `python manage.py check` shows no issues (0 silenced)

### Steps 9–10: First model and admin
- [x] `SiteSettings` model written in `core/models.py`
- [x] Registered in `core/admin.py`

### Step 11: Database and admin account
- [x] `python manage.py makemigrations`
- [x] `python manage.py migrate`
- [x] `python manage.py createsuperuser`

### Step 12: Use the admin
- [x] Superuser account exists and `/admin/` routes respond
- [ ] Add a `SiteSettings` entry in `/admin/` (current database awaiting first row)

---

## Implementation Progress (Commit `f984df2`)

### Models, Views, Routes & Plain Templates
- [x] `Work` model created in `creative/models.py`, registered in `creative/admin.py`
- [x] `SkillGroup`, `Project`, `Education`, `Credential` models in `technical/models.py`, registered in `technical/admin.py`
- [x] Migrations created and applied (`creative/migrations/0001_initial.py`, `technical/migrations/0001_initial.py`)
- [ ] Add sample works, projects, and skills in the admin panel
- [x] `core/views.py` landing view wired to `SiteSettings`
- [x] `creative/views.py` wired to `Work` and `SiteSettings`
- [x] `technical/views.py` wired to `SkillGroup`, `Project`, `Education`, `Credential`, `SiteSettings`
- [x] `config/urls.py` routing `/`, `/creative/`, `/technical/`, and static media serving
- [x] `templates/base.html` base layout skeleton
- [x] `templates/landing.html` shows plain landing page at `/`
- [x] `templates/creative.html` loops works and displays list
- [x] `templates/technical.html` loops skills, projects, education table, and credentials

---

## Next Steps: Phase 1 — Django UI & Polish

### Styling & Interactive Layout
- [x] Landing identity decision recorded: text wordmark only, no round face logo or character illustration
- [ ] Base CSS tokens and Google Fonts (`Inter Tight`, `Playfair Display`, `M PLUS Rounded 1c`, `Michroma`, `Space Mono`) in `templates/base.html` & `static/css/base.css`
- [ ] Landing HTML & CSS: 50/50 vertical split layout in `static/css/landing.css`
- [ ] Creative half styling (royal blue `#1820EF`, cream `#FAFAED`, yellow `#FFC524`, mixed typography, pill CTA)
- [ ] Technical half styling (deep navy `#0c141c`, mint `#87BC87`, Michroma, scanlines overlay)
- [ ] Split hover widening (`flex-grow: 1.35`) on desktop
- [ ] Click navigation with smooth expand animation
- [ ] `landing.js`: desktop seam drag (threshold, flick detection, spring-back)
- [ ] `landing.js`: mobile swipe gestures (stack layout, touch handling)
- [ ] Seam grip line, hint labels, and keyboard accessibility (`tabindex`, arrow navigation)
- [ ] `digits.js`: interactive digit field canvas on the Technical side
- [ ] Creative page styling (`static/css/creative.css`, `static/js/creative.js`): marquee strips, category tab filtering, lightbox modal, About section, contact footer
- [ ] Technical page styling (`static/css/technical.css`): record header stamp, skill boxes, project cards with tech chips, education table, credentials
- [ ] Mobile responsive layout check (< 800px)
- [ ] `prefers-reduced-motion` compliance & visible keyboard focus rings
- [ ] Automated tests in `core/tests.py`, `creative/tests.py`, `technical/tests.py`
- [ ] `collectstatic` verification
- [ ] Deploy Phase 1 (live v1 on Python host)

---

## Phase 2 — API (JSON Endpoints)
- [ ] Install `djangorestframework` and `django-cors-headers`, update `requirements.txt`
- [ ] Configure `settings.py`: `rest_framework`, `corsheaders`, CORS allowed origins (`http://localhost:3000`)
- [ ] Serializers for `SiteSettings`, `Work`, `SkillGroup`, `Project`, `Education`, `Credential`
- [ ] Endpoints: `GET /api/site/`, `GET /api/works/?category=`, `GET /api/technical/`
- [ ] Ensure absolute image URLs via request context
- [ ] API integration tests (`python manage.py test`)

---

## Phase 3 — Next.js Frontend
- [ ] Initialize Next.js in `portfolio/frontend/` (TypeScript, App Router, CSS Modules, no Tailwind)
- [ ] Install Framer Motion, configure `.env.local` (`NEXT_PUBLIC_API_URL`)
- [ ] Configure `next.config.ts` remote image patterns for Django media host
- [ ] Setup `next/font/google` and CSS module variables
- [ ] Define TypeScript types in `lib/types.ts` mirroring Django serializers
- [ ] Implement `SplitLanding` client component with drag & swipe hook (`useSplitDrag`)
- [ ] Seamless route transition with Framer Motion
- [ ] Creative page: animated strips, tab filters, lightbox
- [ ] Technical page: `DigitField` canvas component and record sections
- [ ] Full accessibility, reduced motion, and responsiveness validation
- [ ] Deploy frontend to Vercel, backend to production host (with PostgreSQL & object storage for media)

---

## Optional Enhancements
- [ ] Contact form with email backend
- [ ] Project detail pages (`/technical/projects/<id>/`)
- [ ] Work detail pages / video preview modal
- [ ] Download CV button (`FileField` in `SiteSettings`)
- [ ] Sitemap, `robots.txt`, and Open Graph metadata
