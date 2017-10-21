import sys
import os

from datetime import datetime
from setuptools import setup, Command
from setuptools import find_packages
from setuptools.command.test import test as TestCommand
from setuptools.command.install import install
from setuptools.command.develop import develop
import subprocess
import chimpsetup


setup(
    name='chimpsetup',
    version='0.0.1',
    description='Add extra functionalities to setup',
    long_description='Add extra functionalities to setup',
    keywords='setuptools, dependencies',
    author='Francois Dang Ngoc',
    url='http://github.com/chimpler/chimpsetup',
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    packages=['chimpsetup'],
    tests_require=[
        'pytest'
    ]
)
