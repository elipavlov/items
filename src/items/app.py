# coding=utf-8

from os import sys, path
from logging import getLogger

from .models import install_db, init_db, drop_db
from .view import app

logger = getLogger(__name__)

sys.path.append(path.dirname(path.abspath(__file__)))

logger.info(sys.path)

app = install_db(app)


@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""
    init_db()
    print('Initialized the database.')


@app.cli.command('dropdb')
def initdb_command():
    """Drop all db essences."""
    drop_db()
    print('Dropped the database.')
