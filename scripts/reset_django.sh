#!/bin/bash

pwd

# Remove SQLite database
rm db.sqlite3

# Remove pycache directories
find . -type d -not -path "./.venv/*" -name "__pycache__" -exec rm -rf {} +

# Remove migration files except __init__.py
find . -not -path "./.venv/*" -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -not -path "./.venv/*" -path "*/migrations/*.pyc" -delete

# Run migrations
# python manage.py makemigrations
# python manage.py migrate

# python manage.py createsuperuser
