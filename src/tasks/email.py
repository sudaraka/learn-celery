""" Email task """

from flask import current_app
from flask.ext.mail import Mail, Message

from ..web import celery


@celery.task
def send_email(subject, text):
    """ Send email """

    msg = Message(subject, sender='no-reply@test.com',
                  recipients=['test@test.com'])
    msg.body = text

    mail = Mail(current_app)
    mail.send(msg)
