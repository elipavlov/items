# coding=utf-8

from logging import getLogger
from .config import app

logger = getLogger(__name__)

logger.debug('Package: %s' % __package__)

if __package__ is None:
    __package__ = "items"


__version__ = '0.0.1'
