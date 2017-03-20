#!/usr/bin/env python
# coding=utf-8

import os
import sys
from distutils.core import setup
from setuptools import find_packages


# hardlink issue on vagrant
if os.environ.get('USER', '') == 'vagrant':
    del os.link

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'src'))

version = __import__('items').__version__

install_requires = [
    "flask",
    "flask-sqlalchemy",
    "sqlalchemy-migrate",
]

dev_requires = [
    "pytests",
    "ipdb",
]
mysql_requires = ['MySQL-python']

dependency_links = []

setup(
    name='items',
    version=version,
    package_dir={'items': 'items'},
    packages=find_packages(),
    url='https://items',
    author='Ilya Pavlov',
    author_email='eli.pavlov.vn@gmail.com',
    description='Test service',
    zip_safe=False,
    install_requires=install_requires,
    dependency_links=dependency_links,
    include_package_data=True,
    extras_require={
        'dev': dev_requires,
        'mysql': mysql_requires,
    },
    classifiers=[
        "Framework :: Flask",
        "Framework :: SQL Alchemy",
        "Operating System :: OS Independent"
    ]
)
