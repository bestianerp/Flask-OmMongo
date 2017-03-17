# -*- coding: utf-8 -*-

# Copyright 2015 flask-mongoalchemy authors. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from setuptools import setup

setup(
    name='Flask-OmMongo',
    version='1.0',
    url='http://bapakode.org/flask-ommongo',
    license='BSD',
    author='Bapakode Open Source',
    author_email='opensource@bapakode.org',
    description='Add Flask support for MongoDB using OmMongo.',
    packages=['flask_ommongo'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask>=0.9',
        'OmMongo',
        'pymongo==2.8.1',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
