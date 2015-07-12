""" Celery work module """

from celery import Celery

config = {
    'BROKER_URL': 'redis://localhost',
    'CELERY_RESULT_BACKEND': 'redis://localhost',

    'CELERY_ACCEPT_CONTENT': ['json'],
    'CELERY_TASK_SERIALIZER': 'json',
    'CELERY_RESULT_SERIALIZER': 'json'
}

app = Celery('tasks')
app.conf.update(config)


@app.task
def add(x, y):
    """ Return the sum of x and y """

    return x + y
