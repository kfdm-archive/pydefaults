#!/usr/bin/env python

from pydefaults.osx import osx_database
from pydefaults.plist import plist_database

tests = [
	osx_database('test'),
	plist_database('test'),
]

for db in tests:
	print db.read('test')
	print db.write('testing','value')
