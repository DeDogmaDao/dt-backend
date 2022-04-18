#!/bin/bash
celery -A project worker --loglevel=info -B