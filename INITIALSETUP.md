# INITIALSETUP.md — Django first, then Django API + Next.js

Goal: rebuild the split-screen portfolio (Creative + Technical) as a Django project you can edit from the admin panel. The landing uses a text wordmark only; do not add the round face logo or illustrated character to the landing or detail pages.
This is a guided path with a verification snapshot below. The Django foundation is initialized, but the portfolio pages and content models are still pending.

## Current setup verification — 2026-11-14

The current project is under `portfolio/backend/`. The checks below were run against that directory:

- Python 3.11.1 and Django 5.2.19 are installed in `portfolio/backend/.venv`; the listed Django, Pillow, dotenv, WhiteNoise, and Gunicorn packages import successfully.
- `.env` exists with `SECRET_KEY` and `DEBUG`; settings load a non-default secret and `DEBUG=True`. `.env`, `.venv/`, and `db.sqlite3` are ignored by Git.
- `python manage.py check` passes. `makemigrations --check --dry-run` reports no model changes, and all currently defined migrations are applied.
- SQLite is configured. One Django superuser exists. `/admin/login/` responds in Django's in-process test client.
- The root currently displays Django's debug installation page. A live `runserver` socket could not be confirmed from this environment, so verify it in the owner's terminal.
- `core.SiteSettings` exists and is registered in admin, but the current database contains no `SiteSettings` row.
- `creative` and `technical` are only app shells. They have no models or migrations yet. There are no landing, Creative, or Technical views/templates, and no API or Next.js frontend.
- `portfolio/backend/templates/` is missing even though settings point to it. `portfolio/backend/static/` exists but is empty. WhiteNoise is currently last in `MIDDLEWARE`; this guide places it immediately after `SecurityMiddleware`, so correct that before relying on WhiteNoise for static serving.

**Verdict:** the Django scaffold and database setup are mostly complete; Phase 1 portfolio implementation has not started. The checklist records the remaining setup gaps.

## Roadmap 
| Phase | What you build | What you learn |
|---|---|---|
| 1 | Full Django site: models, admin, templates, your CSS and JS | Backend, ORM, admin, routing |
| 2 | Add a JSON API to the same Django project (Django REST Framework) | APIs, serializers, CORS |
| 3 | New Next.js frontend that reads the API. Django admin stays your dashboard. | React, routing, smooth page transitions |

Do not skip ahead. Phase 1 gives you a working site. Phase 3 replaces only the frontend; your models and admin carry over unchanged.

Repo layout: one folder `portfolio/` containing `backend/` (Django) and, later, `frontend/` (Next.js). Everything in Phases 1 and 2 happens inside `backend/`.

## 0. Is it possible?
Yes. Django serves HTML, data and static files. The target design and interactions are described in `DESIGN.md` and `FEATURES.md`; prototype source files are not part of the current repository. Django adds a database, an admin to edit content, real URLs, and deployment.

| Prototype | Django version |
|---|---|
| One HTML file, content hard-coded | Content in database, edited in `/admin/` |
| Pages are overlays on one page | Three routes: `/`, `/creative/`, `/technical/` |
| Expand animation in place | Same animation, then navigate to the route |
| Landing identity | Text wordmark in the top bar; no round face logo on the landing |

## 1. Prerequisites
- Python 3.11+ (`python --version`)
- Git, a code editor (VS Code)
- Basics: Python functions and classes, HTML, CSS, a little JavaScript

## 2. Create the project
```bash
mkdir -p portfolio/backend && cd portfolio/backend
python -m venv .venv
# Windows: .venv\Scripts\activate     macOS/Linux:
source .venv/bin/activate
pip install "django>=5.2,<6" pillow python-dotenv whitenoise gunicorn
pip freeze > requirements.txt
django-admin startproject config .
python manage.py startapp core
python manage.py startapp creative
python manage.py startapp technical
git init
```
Add a `.gitignore` containing: `.venv/`, `__pycache__/`, `db.sqlite3`, `.env`, `media/`, `staticfiles/`.

## 3. Folder layout
```
portfolio/backend/
├─ config/            settings.py, urls.py
├─ core/              landing page, site settings (bio, links, face)
├─ creative/          Work model, creative page
├─ technical/         Project, Skill, Education, Certification
├─ templates/         base.html, landing.html, creative.html, technical.html
├─ static/
│  ├─ css/            base.css, landing.css, creative.css, technical.css
│  ├─ js/             landing.js, creative.js, digits.js
│  └─ img/            page visuals as needed (no landing face logo)
├─ media/             uploaded work images (admin uploads)
└─ manage.py
```

## 4. Settings (`config/settings.py`)
```python
from pathlib import Path
import os
from dotenv import load_dotenv
load_dotenv()
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv("SECRET_KEY", "dev-only-change-me")
DEBUG = os.getenv("DEBUG", "1") == "1"
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "localhost,127.0.0.1").split(",")

INSTALLED_APPS = [
    # default django apps...
    "core", "creative", "technical",
]
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",   # right after SecurityMiddleware
    # rest of default middleware...
]
TEMPLATES[0]["DIRS"] = [BASE_DIR / "templates"]

STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"
MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"
```
Create `.env`:
```
SECRET_KEY=put-a-long-random-string-here
DEBUG=1
```

## 5. Models

`core/models.py`
```python
from django.db import models

class SiteSettings(models.Model):
    name = models.CharField(max_length=80, default="Tarun Suthar")
    location = models.CharField(max_length=80, default="Indore, IN")
    creative_bio = models.TextField(blank=True)
    technical_bio = models.TextField(blank=True)
    creative_email = models.EmailField(blank=True)
    technical_email = models.EmailField(blank=True)
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    fiverr = models.URLField(blank=True)
    class Meta: verbose_name_plural = "Site settings"
    def __str__(self): return self.name
```

`creative/models.py`
```python
from django.db import models

class Work(models.Model):
    CATEGORIES = [("Personal", "Personal"), ("Stories", "Stories")]
    COLORS = [("blue","Blue"),("grad","Gradient"),("night","Burgundy"),("black","Black"),("white","Cream")]
    ASPECTS = [("3/4","3:4"),("1/1","1:1"),("4/5","4:5"),("16/10","16:10")]
    title = models.CharField(max_length=120)
    category = models.CharField(max_length=20, choices=CATEGORIES)
    color = models.CharField(max_length=10, choices=COLORS, default="blue")
    aspect = models.CharField(max_length=6, choices=ASPECTS, default="1/1")
    image = models.ImageField(upload_to="works/", blank=True)
    order = models.PositiveIntegerField(default=0)
    class Meta: ordering = ["order", "-id"]
    def __str__(self): return self.title
```

`technical/models.py`
```python
from django.db import models

class SkillGroup(models.Model):
    KINDS = [("used","Used in my projects"),("foundation","Foundational knowledge"),("learning","Currently learning")]
    kind = models.CharField(max_length=12, choices=KINDS)
    items = models.TextField(help_text="One skill per line")
    def skill_list(self): return [s for s in self.items.splitlines() if s.strip()]
    def __str__(self): return self.get_kind_display()

class Project(models.Model):
    name = models.CharField(max_length=100)
    meta = models.CharField(max_length=120, blank=True)
    summary = models.TextField()
    bullets = models.TextField(help_text="One bullet per line", blank=True)
    tech = models.CharField(max_length=200, help_text="Comma separated")
    note = models.CharField(max_length=200, blank=True)
    order = models.PositiveIntegerField(default=0)
    class Meta: ordering = ["order"]
    def bullet_list(self): return [b for b in self.bullets.splitlines() if b.strip()]
    def tech_list(self): return [t.strip() for t in self.tech.split(",") if t.strip()]
    def __str__(self): return self.name

class Education(models.Model):
    qualification = models.CharField(max_length=120)
    institution = models.CharField(max_length=160)
    year = models.CharField(max_length=20)
    result = models.CharField(max_length=40, blank=True)
    order = models.PositiveIntegerField(default=0)
    class Meta: ordering = ["order"]

class Credential(models.Model):
    KINDS = [("cert","Certification"),("ach","Achievement")]
    kind = models.CharField(max_length=5, choices=KINDS)
    text = models.CharField(max_length=200)
```

Register all in each app's `admin.py`:
```python
from django.contrib import admin
from .models import Work
admin.site.register(Work)
```
Then:
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

## 6. Views and URLs

`core/views.py`
```python
from django.shortcuts import render
def landing(request): return render(request, "landing.html")
```
`creative/views.py`
```python
from django.shortcuts import render
from core.models import SiteSettings
from .models import Work
def creative(request):
    return render(request, "creative.html", {"works": Work.objects.all(), "site": SiteSettings.objects.first()})
```
`technical/views.py`
```python
from django.shortcuts import render
from core.models import SiteSettings
from .models import *
def technical(request):
    return render(request, "technical.html", {
        "site": SiteSettings.objects.first(),
        "skills": SkillGroup.objects.all(),
        "projects": Project.objects.all(),
        "education": Education.objects.all(),
        "creds": Credential.objects.all(),
    })
```
`config/urls.py`
```python
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from core.views import landing
from creative.views import creative
from technical.views import technical

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", landing, name="landing"),
    path("creative/", creative, name="creative"),
    path("technical/", technical, name="technical"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

## 7. Templates (skeleton)
`templates/base.html`
```html
{% load static %}
<!DOCTYPE html>
<html lang="en"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{% block title %}Tarun Suthar{% endblock %}</title>
<link href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@500;700&family=Playfair+Display:ital,wght@1,500&family=M+PLUS+Rounded+1c:wght@800;900&family=Michroma&family=Space+Mono&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{% static 'css/base.css' %}">
{% block css %}{% endblock %}
</head><body>
{% block body %}{% endblock %}
{% block js %}{% endblock %}
</body></html>
```
`landing.html` extends base: put the two `<section>` halves, the text wordmark, seam grip, and hints. Do not add a face image or illustrated character. Build the page CSS in `landing.css` and interactions in `landing.js`. On click or a committed drag, add the "open" class, wait about 700ms for the animation, then `location.href = "/creative/"` (or `/technical/`).

`creative.html` loops works: `{% for w in works %} <button class="wk k-{{ w.color }}" style="--r:{{ w.aspect }}">{% if w.image %}<img src="{{ w.image.url }}" alt="{{ w.title }}">{% endif %}<span>{{ w.category }}</span></button> {% endfor %}`

`technical.html` loops projects, skills, education, credentials the same way.

## 8. Run
```bash
python manage.py runserver
```
Open http://127.0.0.1:8000/ and http://127.0.0.1:8000/admin/. Add one SiteSettings row, some Works and Projects in the admin.

## 9. Build order (do one step at a time)
1. Landing page static HTML and CSS only (no JS) until it looks right
2. Split hover, then click-to-navigate
3. Seam drag and mobile swipe (`landing.js`)
4. Creative page with hard-coded tiles, then switch to the `Work` model
5. Technical page the same way (digit canvas in `digits.js`)
6. Admin content entry, then polish and accessibility
7. Deploy

## 10. Deploy (when ready)
```bash
python manage.py collectstatic
```
Set `DEBUG=0`, a real `SECRET_KEY` and `ALLOWED_HOSTS` as environment variables. Run with `gunicorn config.wsgi`. Free or cheap options: Render, Railway, PythonAnywhere. For production use PostgreSQL, and store uploaded images on object storage because most hosts reset local disks. Check each host's current Django guide.

## 11. Learning path
Official tutorial at docs.djangoproject.com (polls app), then Django Girls tutorial, then MDN "Django Web Framework". Keep this project as your practice app after the tutorial.


---

# PHASE 2 — Add a JSON API (still inside `backend/`)

Start only when Phase 1 pages and admin work.

## 12. Install
```bash
pip install djangorestframework django-cors-headers
pip freeze > requirements.txt
```
`settings.py`:
```python
INSTALLED_APPS += ["rest_framework", "corsheaders"]
MIDDLEWARE.insert(0, "corsheaders.middleware.CorsMiddleware")   # as high as possible
CORS_ALLOWED_ORIGINS = ["http://localhost:3000"]                # add your Vercel URL later
REST_FRAMEWORK = {"DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.AllowAny"]}
```
The API is read-only in this project. Only GET endpoints, no public writes.

## 13. Serializers and endpoints
`creative/serializers.py`
```python
from rest_framework import serializers
from .models import Work
class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = ["id", "title", "category", "color", "aspect", "image"]
```
`technical/serializers.py`
```python
from rest_framework import serializers
from .models import *
class ProjectSerializer(serializers.ModelSerializer):
    bullets = serializers.ListField(source="bullet_list", read_only=True)
    tech = serializers.ListField(source="tech_list", read_only=True)
    class Meta:
        model = Project
        fields = ["id", "name", "meta", "summary", "bullets", "tech", "note"]
class SkillGroupSerializer(serializers.ModelSerializer):
    items = serializers.ListField(source="skill_list", read_only=True)
    class Meta:
        model = SkillGroup
        fields = ["kind", "items"]
class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ["qualification", "institution", "year", "result"]
class CredentialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Credential
        fields = ["kind", "text"]
```
`core/serializers.py` exposes `SiteSettings` (all fields). Views (`api_views.py` in each app) use `generics.ListAPIView` for lists and a small `APIView` for settings and the combined technical payload.

| Endpoint | Returns |
|---|---|
| `GET /api/site/` | name, location, bios, emails, links |
| `GET /api/works/?category=Personal` | works list (image URL is absolute) |
| `GET /api/technical/` | `{ skills, projects, education, credentials }` |

Image URLs: pass `context={"request": request}` so serializers build absolute URLs.

## 14. Test it
```bash
python manage.py runserver
curl http://127.0.0.1:8000/api/works/
```
Write at least one test per endpoint (`python manage.py test`).

---

# PHASE 3 — Next.js frontend (`frontend/`)

## 15. Prerequisites
Node.js LTS, basics of JavaScript. Learn React first (react.dev "Learn" section) and some TypeScript. Allow time for this. It is the biggest jump in the plan.

## 16. Create the app
```bash
cd ..                      # back to portfolio/
npx create-next-app@latest frontend
# choose: TypeScript yes, ESLint yes, App Router yes, Tailwind no, src dir yes
cd frontend
npm install framer-motion
```
`.env.local`:
```
NEXT_PUBLIC_API_URL=http://127.0.0.1:8000/api
```
`next.config.ts`: allow Django media images via `images.remotePatterns` (protocol, hostname `127.0.0.1`, port `8000`, pathname `/media/**`). Update the host for production.

## 17. Folder layout
```
frontend/src/
├─ app/
│  ├─ layout.tsx            fonts (next/font), global CSS
│  ├─ page.tsx              landing (SplitLanding)
│  ├─ creative/page.tsx     server component, fetches works + site
│  └─ technical/page.tsx    server component, fetches technical + site
├─ components/
│  ├─ SplitLanding.tsx      client: hover, click, seam drag, swipe
│  ├─ DigitField.tsx        client: canvas
│  ├─ WorkStrips.tsx        client: marquee, tab filter, lightbox
│  └─ PageNav.tsx
├─ lib/api.ts               typed fetch helpers
└─ styles/                  landing.module.css, creative.module.css, technical.module.css
```
Fetch pattern (server component):
```ts
const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/works/`, { next: { revalidate: 60 } });
const works: Work[] = await res.json();
```
Keep a TypeScript type for each API response in `lib/types.ts` that mirrors the serializers.

## 18. Port in this order
1. Fonts via `next/font/google`, colour variables in global CSS
2. `SplitLanding` with hover and click (copy your CSS into a CSS module)
3. Seam drag and swipe as a React hook (`useSplitDrag`) using pointer events
4. Smooth open: animate the half to full size with Framer Motion, then `router.push("/creative")`. Detail pages fade in. (Later option: Next.js intercepting routes or the View Transitions API.)
5. Creative page: strips, tabs, lightbox, About
6. Technical page: `DigitField` canvas in `useEffect`, sections from API data
7. Accessibility and `prefers-reduced-motion` (Framer Motion has `useReducedMotion`)
8. Deploy

## 19. Deploy
- Frontend: Vercel (set `NEXT_PUBLIC_API_URL` to the live API URL)
- Backend: Render, Railway or similar with PostgreSQL. Set `DEBUG=0`, `ALLOWED_HOSTS`, `CORS_ALLOWED_ORIGINS`.
- Uploaded images: use object storage (Cloudinary or S3 via django-storages). Local `media/` is usually wiped on redeploy.
- Check each provider's current docs before you start.

## 20. Time budget (beginner, 1–2 h/day)
Phase 1: 4–6 weeks. Phase 2: 3–5 days. Phase 3: 3–5 weeks including React learning. Total about 2.5–3.5 months. With AI help and focus, roughly half.
