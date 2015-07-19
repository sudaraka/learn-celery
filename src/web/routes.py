""" Blueprint """

from flask import Blueprint, request, render_template, url_for, redirect
from flask import current_app
from flask.ext.mail import Mail, Message

blueprint = Blueprint('main', __name__)


@blueprint.route('/', methods=['GET', 'POST'])
def email_form():
    """ Main route """

    if 'GET' == request.method:
        return render_template('form.html')

    subject = request.form.get('subject') or 'Default Subject'
    text = request.form.get('msg') or 'Default message body'

    msg = Message(subject, sender='no-reply@test.com',
                  recipients=['test@test.com'])
    msg.body = text

    mail = Mail(current_app)
    mail.send(msg)

    return redirect(url_for('main.email_form'))
