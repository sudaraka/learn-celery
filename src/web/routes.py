""" Blueprint """

from flask import Blueprint, request, render_template, url_for, redirect

from ..tasks import send_email


blueprint = Blueprint('main', __name__)


@blueprint.route('/', methods=['GET', 'POST'])
def email_form():
    """ Main route """

    if 'GET' == request.method:
        return render_template('form.html')

    subject = request.form.get('subject') or 'Default Subject'
    text = request.form.get('msg') or 'Default message body'

    send_email.delay(subject, text)

    return redirect(url_for('main.email_form'))
