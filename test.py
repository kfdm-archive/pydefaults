#!/usr/bin/env python
import os
import sys
import uuid

def setup(title,d='tdomain',k='tkey',v='tvalue'):
	global domain,key,value
	domain = d
	key = k
	value = v
	print 
	print 'Group:  ',title
	print 'Domain: ',domain
	print 'Key:    ',key
	print 'Value:  ',value
	print '-'*50
def test(title,cmd,chk):
	global domain,key,value
	cmd = cmd.replace('<domain>',domain)
	cmd = cmd.replace('<key>',key)
	cmd = cmd.replace('<value>',value)
	cmd = 'python pydefaults/parser.py %s --debug'%cmd
	pipe = os.popen('{ ' + cmd + '; } 2>&1', 'r')
	txt = pipe.read()
	sts = pipe.close()
	if sts is None: sts = 0
	
	if chk == sts:
		print 'PASSED',title
	else:
		print >> sys.stderr, 'FAILED',title
		print '-'*50
		print >> sys.stderr, cmd
		print >> sys.stderr, sts,test
		print '-'*50
		exit(txt)

setup('Standard Test')
test('Clear test domain','delete "<domain>"',0)
test('Reading missing domain','read "<domain>"',256)
test('Reading missing key','read "<domain>" "<key>"',256)
test('Writing Key','write "<domain>" "<key>" "<value>"',0)
test('Reading domain','read "<domain>"',0)
test('Reading key','read "<domain>" "<key>"',0)
test('Clear test key','delete "<domain>" "<key>"',0)

setup('Invalid Key',k='key = key')
test('Writing Invalid Key','write "<domain>" "<key>" "<value>"',0)
test('Reading Invalid Key','read "<domain>" "<key>"',256)
test('Clear test domain','delete "<domain>"',0)

setup('Rename')
test('Writing Old Key','write "<domain>" "old_key" "<value>"',0)
test('Renaming Key','rename "<domain>" "old_key" new_key',0)
test('Reading New Key','read "<domain>" new_key',0)
test('Reading Old Key','read "<domain>" old_key',256)
