import os
from abc import ABC
from io import StringIO
from celery.utils.log import get_task_logger
from django.core.handlers.wsgi import WSGIRequest
from project import celery_app, settings


class BaseTask(ABC, celery_app.Task):
    name = __name__
    description = ''
    ignore_result = False
    max_retries = 5
    logger = get_task_logger(__name__)

    def run(self, *args, **kwargs):
        return self._run(*args, **kwargs)

    def _run(self, *args, **kwargs):
        raise NotImplementedError

    @property
    def django_request(self):
        host = 'localhost:8000' if settings.DEBUG else os.environ.get("DOMAIN")
        schema = 'https' if os.environ.get('NGINX_SSL') else 'http'
        meta = {
            'wsgi.url_scheme': schema,
            'HTTP_HOST': host,
            'REQUEST_METHOD': 'GET',
            'PATH_INFO': '/',
            'wsgi.input': StringIO(),
        }
        return WSGIRequest(meta)

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        self.logger.error('{0!r} failed: {1!r}'.format(task_id, exc))
        super(BaseTask, self).on_failure(exc, task_id, args, kwargs, einfo)
