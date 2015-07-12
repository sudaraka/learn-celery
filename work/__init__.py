""" Celery work module """

from celery import Celery

from .config import celery_config


app = Celery('tasks')
app.config_from_object(celery_config)

from .tasks.add import add
