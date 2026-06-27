# Yasir Naeem — Portfolio Website

A clean, professional, responsive single-page portfolio website built with Django and Python.

## Live Site

**GitHub Pages:** https://yasir897.github.io

## Features

- Responsive single-page design (Desktop, Tablet, Mobile)
- **Hero Section** — Name, title, photo, and call-to-action buttons
- **About Section** — Bio, contact details, quick stats
- **Skills Section** — Progress bars by category
- **Education Section** — Vertical timeline
- **Projects Section** — Cards with GitHub & live links
- **Contact Section** — Working contact form saved to database
- **Django Admin Panel** — Manage all content from /admin/

## Technologies

- **Backend:** Python 3.12, Django 6.0
- **Database:** SQLite
- **Frontend:** HTML5, CSS3, Vanilla JavaScript
- **Icons:** Font Awesome 6
- **Fonts:** Poppins (Google Fonts)

## Project Structure

```
YasirPortfolio/
├── YasirPortfolio/      # Django project settings
├── portfolio/           # Main Django app
│   ├── models.py        # Profile, Skill, Education, Project, ContactMessage
│   ├── views.py         # Home view + contact form handler
│   ├── admin.py         # Admin panel configuration
│   └── urls.py
├── static/
│   ├── css/style.css
│   ├── js/main.js
│   ├── images/
│   └── files/
├── templates/home.html  # Main template
├── media/               # Uploaded images
├── fixtures/            # Initial data
├── manage.py
└── requirements.txt
```

## Installation & Setup

### 1. Prerequisites
Make sure Python 3.10+ is installed.

### 2. Navigate to project
```bash
cd YasirPortfolio
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Load initial data (optional)
```bash
python manage.py loaddata fixtures/initial_data.json
```

### 6. Create admin user
```bash
python manage.py createsuperuser
```

### 7. Run the server
```bash
python manage.py runserver
```

### 8. Open in browser
- **Portfolio:** http://127.0.0.1:8000/
- **Admin Panel:** http://127.0.0.1:8000/admin/

## Admin Credentials (local dev)

- **Username:** admin
- **Password:** admin1234

## Managing Content

Log into the admin panel at `/admin/` to:
- Edit your **Profile** (name, title, about, contact info, profile picture)
- Add/edit **Skill Categories** and **Skills**
- Manage **Education** entries
- Add **Projects** with GitHub links
- View **Contact Messages** submitted via the form
