# coding=utf-8

import os

from flask import Flask

app = Flask(__name__)

conf = type('Config', (), {})()

conf.DEBUG = True
conf.SQLALCHEMY_DATABASE_URI = \
    os.environ.get(
        'SQLALCHEMY_DATABASE_URI',
        'sqlite:///{}'.format(os.path.join(app.root_path, 'project.db')))

conf.SQLALCHEMY_TRACK_MODIFICATIONS = True
# print(conf.SQLALCHEMY_DATABASE_URI)

conf.SECRET_KEY = 'secret meow 666'
conf.API_PATH = '/api/v1/'

app.config.from_object(conf)

# app.config.update(dict(
# ))

