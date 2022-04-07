#!/bin/bash
python3 manage.py migrate
python3 manage.py collectstatic --noinput
python3 manage.py compilemessages
gunicorn -c /scripts/gunicorn.conf.py project.wsgi