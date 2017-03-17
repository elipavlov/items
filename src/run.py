# coding=utf-8

from os import sys, path
from logging import getLogger

from items.view import app

sys.path.append(path.dirname(path.abspath(__file__)))

logger = getLogger(__name__)
logger.info(sys.path)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)





