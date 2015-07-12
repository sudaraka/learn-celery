""" Example celery task """

from .. import app


@app.task
def add(x, y):
    """ Return the sum of x and y """

    return x + y
