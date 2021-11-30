#!/usr/bin/env python

import os, sys
from codecs import open
from setuptools import setup

WORK_DIR = os.path.abspath(os.path.dirname(__file__))

# sys.path.insert(0, os.path.join(WORK_DIR, 'kp_committee'))
from version import VERSION

with open(os.path.join(WORK_DIR, 'README.md'), mode='r', encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()


# This setup is suitable for "python setup.py develop".
setup(
        name='kp_committee',

        version=VERSION,

        description='Knapsack problem and committee selection',

        author='Roman Overko',

        author_email=['roman.overko@iota.org'],

        url='https://github.com/roman1e2f5p8s/kp_committee',

        # packages=[''],

        license='none',

        keywords='committee selection, knapsack problem',

        # install_requires='',

        # tests_require=['pytest'],

        # setup_requires=['pytest-runner'],

        classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 1 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Science/Research',
        'Topic :: Libraries :: Python Modules',

        # Pick your license as you wish (should match "license" above)
        # 'License :: OSI Approved :: Apache Software License',

        'Programming Language :: Python :: 3.9',
    ],
)
