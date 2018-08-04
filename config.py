# -*- coding: utf-8 -*-

import os

base_dir = os.path.abspath(os.path.dirname(__file__))

class Config(object):

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'ASDNL<K#JUO@o2i3u10lsadh;lsa213dfJASID932'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(base_dir, 'coffe.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    