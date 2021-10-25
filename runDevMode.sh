#!/bin/bash

set -e 

echo "Check if database is created..."
if [ ! -f './databases/db.sqlite3' ]; then
    echo "Database is not created....[migrating]"
    python manage.py shell < ./databases/loadSemanticDatabase.py
    python manage.py migrate;
    python manage.py loaddata seed.json;
    echo "[migrated]"
fi

python manage.py runserver 0.0.0.0:8000;