#!/bin/bash

# Remove SQLite database
rm db.sqlite3

# Remove pycache
rg --files --hidden --glob '!.git/*' '(__pycache__|\.pyc|\.pyo$)' | xargs rm -rf

# Remove migrations
rg --files --hidden --glob '!.git/*' '*.py' | rg -v '__init__.py' | rg 'migrations' | xargs rm -rf

# Run migrations
python manage.py makemigrations
python manage.py migrate
