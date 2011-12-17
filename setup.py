#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
	name='pydefaults',
	version='0.0.1',
	packages=['pydefaults'],
	scripts=['scripts/pydefaults'],
	)