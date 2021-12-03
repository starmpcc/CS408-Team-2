#!/usr/bin/env python
import os, sys

from app import create_app, db
from flask_script import Manager, Shell, Server

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)


def make_shell_context():
    return dict(app=app, db=db)


manager.add_command("Shell", Shell(make_context=make_shell_context))
manager.add_command("runserver", Server(host="0.0.0.0", port=5000, threaded=True))

if __name__ == "__main__":
    manager.run()
