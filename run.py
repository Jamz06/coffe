# -*- coding: utf-8 -*-
from app import app, db

from app.models import User, Operation, Customer


@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'User': User,
        'Operation': Operation,
        'Customer': Customer
    }
