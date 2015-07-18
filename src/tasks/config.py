""" Celery work configuration """

celery_config = {
    'BROKER_URL': 'redis://localhost',
    'CELERY_RESULT_BACKEND': 'redis://localhost',

    'CELERY_ACCEPT_CONTENT': ['json'],
    'CELERY_TASK_SERIALIZER': 'json',
    'CELERY_RESULT_SERIALIZER': 'json'
}
