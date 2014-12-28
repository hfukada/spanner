#!/usr/bin/env python

from distutils.core import setup
from toolbelt import __version__

setup(
    name='toolbelt',
    version=__version__,
    description='An esoteric accumulation of frequently used utilities / convenience functions for python',
    author='Bryan Johnson',
    author_email='d.bryan.johnson@gmail.com',
    packages=['toolbelt'],
    url='https://github.com/dbjohnson/python-utils',
    download_url='https://github.com/dbjohnson/toolbelt/tarball/%s' % __version__
)
