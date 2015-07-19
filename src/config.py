""" Web application configuration """


class Config(object):
    """ Web server configuration """

    DEBUG = True

    MAIL_SERVER = 'localhost'
    MAIL_PORT = 8025

    BROKER_URL = 'redis://localhost'
    CELERY_RESULT_BACKEND = 'redis://localhost'

    CELERY_ACCEPT_CONTENT = ['json']
    CELERY_TASK_SERIALIZER = 'json'
    CELERY_RESULT_SERIALIZER = 'json'
