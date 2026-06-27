# Yasir Naeem — Portfolio Website

A clean, professional, and fully responsive single-page portfolio website built with Django and Python as a Web Technologies university project.

## Live Demo

**Live Site:** https://yasir897.pythonanywhere.com

**Admin Panel:** https://yasir897.pythonanywhere.com/admin/

---

## Features

- Fully responsive design (Desktop, Tablet, Mobile)
- **Home / Hero Section** — Name, title, profile photo, and action buttons
- **About Section** — Bio, contact info, and quick stats
- **Skills Section** — Skill categories with animated progress bars
- **Education Section** — Vertical timeline layout
- **Projects Section** — Cards with GitHub and Live Demo links
- **Contact Section** — Working contact form (saves to database)
- **Django Admin Panel** — Manage all content without touching code

---

## Technologies Used

| Layer | Technology |
|-------|-----------|
| Backend | Python 3.12, Django 6 |
| Database | SQLite |
| Frontend | HTML5, CSS3, Vanilla JavaScript |
| Icons | Font Awesome 6 |
| Fonts | Poppins (Google Fonts) |
| Hosting | PythonAnywhere |

---

## Project Structure

```
YasirPortfolio/
│
├── YasirPortfolio/          # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── portfolio/               # Main Django app
│   ├── models.py            # Profile, SkillCategory, Skill, Education, Project, ContactMessage
│   ├── views.py             # Home view + contact form handler
│   ├── admin.py             # Admin panel configuration
│   ├── urls.py
│   └── migrations/
│
├── static/
│   ├── css/style.css        # All styles (teal-violet theme)
│   ├── js/main.js           # Scroll animations, navbar, progress bars
│   ├── images/              # Profile image
│   └── files/               # Resume file
│
├── templates/
│   └── home.html            # Single-page template
│
├── media/                   # Uploaded images (via admin)
├── fixtures/
│   └── initial_data.json    # Pre-loaded portfolio data
│
├── manage.py
├── requirements.txt
└── README.md
```

---

## Django Models

| Model | Fields |
|-------|--------|
| `Profile` | name, title, tagline, about, email, phone, location, github_url, linkedin_url, profile_picture |
| `SkillCategory` | name, order |
| `Skill` | category, name, proficiency (0–100), order |
| `Education` | degree, institution, duration, description, order |
| `Project` | title, description, technologies, github_url, live_url, image, is_featured, order |
| `ContactMessage` | name, email, message, submitted_at |

---

## Local Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/Yasir897/web-project-portfolio.git
cd web-project-portfolio
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run database migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Load initial data
```bash
python manage.py loaddata fixtures/initial_data.json
```

### 5. Create admin user
```bash
python manage.py createsuperuser
```

### 6. Collect static files
```bash
python manage.py collectstatic --noinput
```

### 7. Start the development server
```bash
python manage.py runserver
```

### 8. Open in browser
- **Portfolio:** http://127.0.0.1:8000/
- **Admin Panel:** http://127.0.0.1:8000/admin/

---

## Admin Credentials (Local Development)

| Field | Value |
|-------|-------|
| Username | `admin` |
| Password | `admin1234` |

---

## Managing Content via Admin Panel

Log into `/admin/` to manage everything without touching any code:

- **Profile** — Edit name, title, bio, contact info, upload profile picture
- **Skill Categories & Skills** — Add/edit skills with proficiency percentages
- **Education** — Add degrees and institutions
- **Projects** — Add projects with GitHub links, live demo URLs, and images
- **Contact Messages** — View all messages submitted through the contact form

---

## PythonAnywhere Deployment

```bash
# On PythonAnywhere Bash console:
git clone https://github.com/Yasir897/web-project-portfolio.git ~/YasirPortfolio
cd ~/YasirPortfolio
pip3.12 install django pillow --user
python3.12 manage.py migrate
python3.12 manage.py loaddata fixtures/initial_data.json
python3.12 manage.py collectstatic --noinput
python3.12 manage.py createsuperuser
```

**WSGI file** (`/var/www/yasir897_pythonanywhere_com_wsgi.py`):
```python
import sys, os
path = '/home/yasir897/YasirPortfolio'
if path not in sys.path:
    sys.path.insert(0, path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'YasirPortfolio.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

**Static files** (Web tab → Static files):
- `/static/` → `/home/yasir897/YasirPortfolio/staticfiles`
- `/media/` → `/home/yasir897/YasirPortfolio/media`

---

## Author

**Yasir Naeem**
- GitHub: [Yasir897](https://github.com/Yasir897)
- LinkedIn: [yasir-naeem](https://www.linkedin.com/in/yasir-naeem-a5176a321/)
- Email: yasir007naeem@gmail.com
- Live Portfolio: https://yasir897.pythonanywhere.com
