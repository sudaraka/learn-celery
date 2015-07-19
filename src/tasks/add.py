""" Example celery task """

from ..web import celery


@celery.task
def add(x, y):
    """ Return the sum of x and y """

    return x + y
