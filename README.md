# Celery Example

Practice code created while following:

  - [Celery Documentation](http://docs.celeryproject.org/en/latest/)
  - [Using Celery With Flask](http://blog.miguelgrinberg.com/post/using-celery-with-flask) &
  - [Celery and the Flask Application Factory Pattern](http://blog.miguelgrinberg.com/post/celery-and-the-flask-application-factory-pattern) by [Miguel Grinberg](https://twitter.com/miguelgrinberg)

## Install

Install `celery` and `flask` modules into python3 virtual environment using
provided `requirements.txt`.

    python -m venv .env
    . .env/bin/activate
    pip install -r requirements.txt

Optionally, install `supervisord` and `redis` globally via system package
manager.

__Note:__ Do NOT install `supervisord` via `pip` as we are using  Python 3 which
is not compatible with supervisord.

## Usage

Start `supervisord` using the etc/supervisord.conf, this will start:

1. Flask web server.
2. Celery worker
3. Python SMTP debugging daemon

Run `redis` instance on the default port.

### Simple task

With `supervisord` running, start monitoring Celery output in one terminal...

    supervisorctl tail -f celery

...run following for test

    python
    >>> from src.tasks import add
    >>> from src.web import create_app
    >>> app = create_app()
    >>> app.app_context().push()
    >>> r = add.delay(5, 3)
    >>> r.get()
    8

### Sending emails from Flask

With `supervisord` running, start monitoring Celery output in one terminal...

    supervisorctl tail -f celery

...start monitoring SMTP daemon output in another terminal

    supervisorctl tail -f smtpd

Finally open http://127.0.0.1:5000/, submit the form and inspect the console for
email message.

## Note on `supervisord` and Python output

By default all console out put of Python programs are buffered. This will cause
the `supervisorctl tail -f ...` output to either not show up instantly or not
show up at all. As a workaround for this pass `-u` argument to Python
interpreter.

## License

Copyright (c) 2015, [Sudaraka Wijesinghe](http://sudaraka.org)
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
