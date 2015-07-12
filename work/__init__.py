""" Celery work module """

from celery import Celery

from .config import celery_config


app = Celery('tasks')
app.config_from_object(celery_config)


@app.task
def add(x, y):
    """ Return the sum of x and y """

    return x + y
