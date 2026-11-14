# CHECKLIST.md — Portfolio build progress

Legend: `[x]` verified complete · `[~]` partial or not confirmed · `[ ]` to do.
Progress below reflects the files and database checked on 2026-11-14, not just commands previously suggested.

---

## Planning and docs
- [ ] Prototype source for the landing, Creative, and Technical pages is not present in this project tree.
- [x] `DESIGN.md`, `FEATURES.md`, `AGENTS.md`, and `INITIALSETUP.md` are present as planning documents.
- [x] The current implementation phase is the Django foundation in `portfolio/backend/`.

---

## Guided setup — chat 1 (Steps 1–6)

### Step 1: Check tools
- [x] Python 3.11.1 is available in the backend virtual environment
- [x] Git 2.53.0 is available

### Step 2: Folders and virtual environment
- [x] Created `portfolio/backend` and entered it
- [x] `.venv` exists in `portfolio/backend/`
- [~] Activation is session-specific; this audit ran commands using the virtual environment's Python directly

### Step 3: Install packages
- [x] Django 5.2.19, Pillow, python-dotenv, WhiteNoise, and Gunicorn are installed and import successfully
- [x] `requirements.txt` is present with pinned dependencies
- [x] Django version command reports 5.2.19

### Step 4: Project and apps
- [x] `django-admin startproject config .`
- [x] Created apps `core`, `creative`, `technical`
- [x] `manage.py` sits directly inside `backend/`

### Step 5: First run
- [x] Built-in and `core` migrations are applied
- [~] Django's root debug page responds in-process, but a live `runserver` connection was not confirmed from this environment

### Step 6: Git
- [x] `git init`
- [x] `.gitignore` created (`.venv/`, `__pycache__/`, `db.sqlite3`, `.env`, `media/`, `staticfiles/`)

---

## Guided setup — chat 2 (Steps 7–12)

### Step 7: `.env`
- [x] `.env` has a configured non-default `SECRET_KEY` and `DEBUG=1` (the secret value was not printed)

### Step 8: `config/settings.py`
- [x] 8a: imported `os` and `load_dotenv()`
- [x] 8b: `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS` read from environment
- [x] 8c: added `core`, `creative`, `technical` to `INSTALLED_APPS`
- [ ] 8d: WhiteNoise is installed but currently last in `MIDDLEWARE`; move it directly after `SecurityMiddleware`
- [~] 8e: `TEMPLATES['DIRS']` points to `templates/`, but the directory is missing
- [~] 8f: static and media settings are configured; `static/` exists but is empty
- [x] `python manage.py check` shows no issues

### Steps 9–10: First model and admin
- [x] `SiteSettings` model written in `core/models.py`
- [x] Registered in `core/admin.py`

### Step 11: Database and admin account
- [x] `python manage.py makemigrations`
- [x] `python manage.py migrate`
- [x] `python manage.py createsuperuser`

### Step 12: Use the admin
- [~] One superuser exists and `/admin/login/` responds, but a successful login was not verifiable in this audit
- [ ] Add a Site settings entry; the current database contains zero `SiteSettings` rows

---

## Future checkpoints

### Next chunk: more models and the first real page
- [ ] `Work` model in `creative/models.py`, registered in admin
- [ ] `SkillGroup`, `Project`, `Education`, `Credential` models in `technical/models.py`, registered in admin
- [ ] `makemigrations` and `migrate` again
- [ ] Add sample works, projects and skills in the admin
- [ ] `core/views.py` landing view
- [ ] `config/urls.py` with `/`, `/creative/`, `/technical/`, media serving
- [ ] `templates/base.html` with fonts and static links
- [ ] `templates/landing.html` shows a plain page at `/`

### Phase 1 — Django site
- [x] Landing identity decision recorded: text wordmark only, no round face logo or character illustration
- [ ] Landing HTML and CSS: 50/50 split, no JavaScript yet
- [ ] Creative half styling (royal blue, mixed type, pill button, tilted cards)
- [ ] Technical half styling (deep navy, mint text, Michroma, scanlines)
- [ ] Hover widening
- [ ] Click animates, then navigates to the route
- [ ] `landing.js`: seam drag on desktop (threshold, flick, spring-back)
- [ ] `landing.js`: swipe up and down on mobile
- [ ] Hint labels, grip line, keyboard support
- [ ] `digits.js`: digit field canvas on the Technical half
- [ ] Creative page: nav, hero, strips from the `Work` model, tab filter, lightbox, About, contact
- [ ] Technical page: nav, record header, skills, projects, education, credentials, contact
- [ ] Mobile layout check at narrow widths
- [ ] `prefers-reduced-motion` and keyboard focus check
- [ ] Write a few tests (`python manage.py test`)
- [ ] `collectstatic`, set production environment variables
- [ ] Deploy Phase 1 (v1 live)

### Phase 2 — API
- [ ] Install `djangorestframework` and `django-cors-headers`, update `requirements.txt`
- [ ] Settings: apps, CORS middleware, allowed origin `http://localhost:3000`
- [ ] Serializers for Site settings, Work, Technical models
- [ ] Endpoints: `/api/site/`, `/api/works/`, `/api/technical/`
- [ ] Test with `curl`
- [ ] Tests for each endpoint

### Phase 3 — Next.js
- [ ] Install Node.js LTS and learn React basics
- [ ] `npx create-next-app@latest frontend` (TypeScript, App Router, no Tailwind)
- [ ] Install Framer Motion, add `.env.local` and `next.config.ts` image host
- [ ] Fonts with `next/font`, colour variables in global CSS
- [ ] `lib/types.ts` and `lib/api.ts`
- [ ] `SplitLanding` with hover and click
- [ ] `useSplitDrag` hook (desktop drag and mobile swipe)
- [ ] Smooth expand-to-page transition
- [ ] Creative page with strips, tabs, lightbox, About
- [ ] Technical page with `DigitField` and sections from the API
- [ ] Accessibility and reduced motion
- [ ] Deploy frontend (Vercel) and backend (Python host, PostgreSQL, image storage)
- [ ] Final check: same visuals and gestures as v1

### Optional later
- [ ] Contact form
- [ ] Project detail pages
- [ ] Download CV button
- [ ] Sitemap, robots.txt, Open Graph image
