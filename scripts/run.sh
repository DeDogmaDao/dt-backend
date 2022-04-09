#!/bin/bash
python3 /app/project/src/manage.py migrate
python3 /app/project/src/manage.py collectstatic --noinput
#python3 manage.py compilemessages # TODO: translation
cd src && gunicorn -c /app/project/scripts/gunicorn.conf.py project.wsgi