# -*- coding: utf-8 -*-

# Copyright 2015 flask-mongoalchemy authors. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from setuptools import setup

LONG_DESCRIPTION = open('README.md', 'r').read()

setup(
    name='Flask-OmMongo',
    version='1.1.1',
    url='https://github.com/bapakode/Flask-OmMongo',
    license='BSD',
    author='Bapakode Open Source',
    author_email='opensource@bapakode.com',
    description='Add Flask support for MongoDB using OmMongo.',
	long_description=LONG_DESCRIPTION,
	long_description_content_type='text/markdown',
    packages=['flask_ommongo'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask>=0.9',
        'OmMongo',
        'pymongo>=2.8.1',
		'pytz'
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
