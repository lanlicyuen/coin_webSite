# Coin Store

Simple Django-based site for showcasing collectible gold and silver coins.

## Features
- Manage products from Django Admin
- Display featured products on the homepage
- Tailwind CSS styling for a clean, premium look

## Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run migrations and create a superuser:
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```
3. Start the development server:
   ```bash
   python manage.py runserver
   ```
   Media files will be served from `/media/` during development.
