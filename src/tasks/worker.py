""" Celery worker """

from celery import Celery

from .config import celery_config


celery = Celery('tasks')
celery.config_from_object(celery_config)
