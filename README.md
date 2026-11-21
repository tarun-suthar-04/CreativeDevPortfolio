# Tarun Suthar — Portfolio (Dual-Personality Split Site)

> **One person, two identities:** AI Creative Artist & Visual Content Creator on one side; Software Developer & Computer Science Graduate on the other.

A custom portfolio web application designed around an interactive 50/50 split landing screen that routes into two distinct, branded worlds:
- **Creative (`/creative/`)**: Funky, editorial, and playful. Royal blue (`#1820EF`), cream (`#FAFAED`), and yellow (`#FFC524`). Showcasing AI artwork, motion experiments, and digital storytelling.
- **Technical (`/technical/`)**: Corporate-sci-fi terminal inspired by *Severance* / Lumon. Deep navy (`#0c141c`) and mint (`#87BC87`) with CRT scanlines and an interactive digit field. Showcasing software engineering projects, backend systems, skills, and academic credentials.

---

## 🚀 Project Roadmap & Current Phase

This project is built in three intentional phases, serving as both a production portfolio and a hands-on learning journey in full-stack architecture:

| Phase | Description | Status | Stack |
|---|---|---|---|
| **Phase 1** | **Full-Stack Django Site** | **In Progress** 🟡 | Django 5.2, Python 3.11+, SQLite, Plain HTML/CSS/JS |
| **Phase 2** | **Headless JSON API** | Planned ⚪ | Django REST Framework, CORS Headers |
| **Phase 3** | **Next.js Frontend (v2)** | Planned ⚪ | Next.js (App Router), TypeScript, CSS Modules, Framer Motion |

> [!IMPORTANT]
> **Current Milestone (Phase 1):**
> - Django project configuration, database models (`SiteSettings`, `Work`, `SkillGroup`, `Project`, `Education`, `Credential`), admin customization, URL routing, and functional skeleton templates are complete.
> - **Next Up:** Static CSS & JS authoring (50/50 split layout, desktop seam drag, mobile swipe, typography tokens, digit canvas, marquee strips) and sample data entry in `/admin/`.

---

## 📁 Repository Structure

```text
CDportfolio/
├── AGENTS.md            # Guidelines and rules for AI coding assistants
├── CHECKLIST.md         # Comprehensive progress tracker and task checklist
├── CreativeInfo.md      # Creative background, toolkit, philosophy, and copy
├── TechnicalInfo.md     # Engineering background, education, projects, and skills
├── DESIGN.md            # Design system, brand tokens, typography, and motion specs
├── FEATURES.md          # Feature matrix across Phase 1, Phase 2, and Phase 3
├── INITIALSETUP.md      # Step-by-step setup walkthrough and implementation guide
├── README.md            # Project overview, architecture, and developer guide
├── .vscode/             # Editor configuration
└── portfolio/
    ├── backend/         # Django project root (Active workspace)
    │   ├── config/      # Project settings, WSGI, ASGI, root URL routing
    │   ├── core/        # Landing page, SiteSettings singleton model
    │   ├── creative/    # Creative showcase: Work model, admin, views
    │   ├── technical/   # Technical portfolio: SkillGroup, Project, Education, Credential
    │   ├── templates/   # HTML templates (base.html, landing.html, creative.html, technical.html)
    │   ├── static/      # Static assets (css/, js/, img/)
    │   ├── media/       # Uploaded images from Django admin (git-ignored)
    │   ├── db.sqlite3   # Development SQLite database (git-ignored)
    │   ├── manage.py    # Django command-line runner
    │   └── requirements.txt # Python package dependencies
    └── frontend/        # Next.js application (Phase 3 - to be initialized)
```

---

## 🛠️ Tech Stack (Phase 1)

- **Framework:** [Django 5.2 LTS](https://docs.djangoproject.com/en/5.2/)
- **Language:** Python 3.11+
- **Database:** SQLite (local development) / PostgreSQL (production target)
- **Asset Serving:** [WhiteNoise 6.12](https://whitenoise.readthedocs.io/)
- **Image Processing:** [Pillow 13.0](https://pillow.readthedocs.io/)
- **Environment Management:** `python-dotenv`
- **WSGI Server:** Gunicorn

---

## ⚙️ Quick Start & Local Development

All commands run inside `portfolio/backend/`.

### 1. Prerequisites
- Python 3.11 or higher
- Git

### 2. Setup Virtual Environment

**Windows (PowerShell / Command Prompt):**
```powershell
cd "portfolio\backend"
python -m venv .venv
.\.venv\Scripts\activate
```

**macOS / Linux:**
```bash
cd portfolio/backend
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Environment Variables
Create a `.env` file inside `portfolio/backend/`:
```env
SECRET_KEY=your-secure-random-secret-key
DEBUG=1
ALLOWED_HOSTS=localhost,127.0.0.1
```

### 5. Run Migrations & Setup Admin
```bash
python manage.py migrate
python manage.py createsuperuser
```

### 6. Verify System Check & Start Server
```bash
python manage.py check
python manage.py runserver
```

Open your browser to:
- **Landing Gateway:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Creative Side:** [http://127.0.0.1:8000/creative/](http://127.0.0.1:8000/creative/)
- **Technical Side:** [http://127.0.0.1:8000/technical/](http://127.0.0.1:8000/technical/)
- **Django Admin:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 📊 Data Models & CMS

All content is managed through Django's admin without hardcoded portfolio text in templates:

1. **`core.SiteSettings`**: Singleton for owner identity, location, creative bio, technical bio, emails, and social links (GitHub, LinkedIn, Fiverr).
2. **`creative.Work`**: Portfolio pieces featuring title, category (`Personal`, `Stories`), aspect ratios (`3:4`, `1:1`, `4:5`, `16:10`), color theme tokens, order, and image upload.
3. **`technical.SkillGroup`**: Categorized skills (`Used in my projects`, `Foundational knowledge`, `Currently learning`) parsed into lists.
4. **`technical.Project`**: Engineering projects (name, summary, bullet points, tech stack tags, notes).
5. **`technical.Education`**: Academic history (qualification, institution, year, result/grade).
6. **`technical.Credential`**: Certifications and achievements.

---

## 🎨 Design Rules & Brand Identity

*Refer to [DESIGN.md](file:///d:/CreativeDev%20Portfolio/CDportfolio/DESIGN.md) for full design specifications.*

- **Dual Branding:** The Creative and Technical sides must appear as two completely separate brands. Never mix their typography or color palettes.
- **Brand Tokens:**
  - *Creative:* `--royal: #1820EF`, `--cream: #FAFAED`, `--yellow: #FFC524`, `--cherry: #FF4E42`, `--burgundy: #832626`.
  - *Technical:* `--deep: #0c141c`, `--mint: #87BC87`, `--pale-mint: #d6efd6`, `--teal: #73B3C5`.
- **Typography:**
  - *Creative:* Inter Tight, Playfair Display italic, M PLUS Rounded 1c.
  - *Technical:* Michroma, Space Mono.
- **Gateway Rules:**
  - Landing gateway uses a clean text wordmark (`Tarun Suthar`) only.
  - Do **not** render a round face logo on the seam or the illustrated full-body character portrait on any page.
- **Accessibility:** Full support for `prefers-reduced-motion`, visible focus outlines, and keyboard navigation.

---

## 📜 Commit History & Evolution

| Commit | Date | Summary | Key Additions |
|---|---|---|---|
| `7697580` | 2026-11-14 | *Initial Django portfolio setup* | Scaffolding for `config`, `core`, `creative`, `technical`, `.env`, initial `requirements.txt`, `SiteSettings` model. |
| `6b5d99d` | 2026-11-21 | *fixed loose ends* | Relocated `WhiteNoiseMiddleware` immediately following `SecurityMiddleware` in `settings.py`; `.vscode` config. |
| `f984df2` | 2026-11-21 | *Add models, admin, views and plain pages* | Added `Work`, `SkillGroup`, `Project`, `Education`, `Credential` models; registered all in admin; views for `/`, `/creative/`, `/technical/`; added `templates/` with `base.html`, `landing.html`, `creative.html`, `technical.html`. |

---

## 📚 Documentation Quick Links

- [AGENTS.md](file:///d:/CreativeDev%20Portfolio/CDportfolio/AGENTS.md) — Coding agent rules, owner context, and constraints.
- [CHECKLIST.md](file:///d:/CreativeDev%20Portfolio/CDportfolio/CHECKLIST.md) — Step-by-step feature and phase progress tracker.
- [DESIGN.md](file:///d:/CreativeDev%20Portfolio/CDportfolio/DESIGN.md) — Color palettes, typography, components, and animations.
- [FEATURES.md](file:///d:/CreativeDev%20Portfolio/CDportfolio/FEATURES.md) — Specification and mapping across phases.
- [INITIALSETUP.md](file:///d:/CreativeDev%20Portfolio/CDportfolio/INITIALSETUP.md) — Architectural overview, code snippets, and setup instructions.
- [CreativeInfo.md](file:///d:/CreativeDev%20Portfolio/CDportfolio/CreativeInfo.md) — Creative background, toolkit, and bio copy.
- [TechnicalInfo.md](file:///d:/CreativeDev%20Portfolio/CDportfolio/TechnicalInfo.md) — Technical background, education, projects, and certifications.
