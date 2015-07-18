#!/usr/bin/env python
"""
manage.py: run application related commands
"""

import os
import sys

sys.path.append(os.path.dirname('..'))

from flask.ext.script import Manager

from src.web import create_app


app = create_app()
manager = Manager(app)

if '__main__' == __name__:
    manager.run()
