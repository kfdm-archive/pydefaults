import os
from optparse import OptionParser
from defaults import defaults,Error

class ClientParser(OptionParser):
	def __init__(self):
		usage = '''usage: %prog [options]
	read
	read <domain>
	read <domain> <key>

	write <domain> <key> <value>
	
	rename <domain> <old_key> <new_key>
	
	delete <domain>
	delete <domain> <key>
'''
		OptionParser.__init__(self,usage=usage)
		self.add_option("-H","--host",help="Hostname",
						dest='host',default='~/.defaults')
		self.add_option("-e","--edit",help="Open file in editor",
						dest='edit',action="store_true",default=False)
		self.add_option("-d","--debug",help="Extra debug information",
						dest='debug',action="store_true",default=False)
	def parse_args(self, args=None, values=None):
		opts, args = OptionParser.parse_args(self, args, values)
		if opts.debug:
			print opts
			print args
		if opts.edit:
			if os.environ['EDITOR']:
				os.system('%s %s'%(os.environ['EDITOR'],opts.host))
			exit()
		if len(args) < 1: exit(self.print_help())
		values = defaults(opts.host)
		if args[0] not in ['read','write','rename','delete']:
			self.error('Unknown command %s'%args[0])
		if args[0] == 'read':
			try:
				if len(args) == 1:
					print values.read()
				elif len(args) == 2:
					print values.read(args[1])
				elif len(args) == 3:
					print values.read(args[1],args[2])
				else:
					self.error('Invalid Arguments')
			except Error,e:
				if not opts.debug: exit(e)
				raise e
		if args[0] == 'write':
			try:
				if len(args) == 4:
					print values.write(args[1],args[2],args[3])
				else:
					self.error('Invalid Arguments')
			except Error,e:
				if not opts.debug: exit(e)
				raise e
		if args[0] == 'rename':
			try:
				if len(args) == 4:
					print values.rename(args[1],args[2],args[3])
				else:
					self.error('Invalid Arguments')
			except Error,e:
				if not opts.debug: exit(e)
				raise e
		if args[0] == 'delete':
			try:
				if len(args) == 2:
					print values.delete(args[1])
				elif len(args) == 3:
					print values.delete(args[1],args[2])
				else:
					self.error('Invalid Arguments')
			except Error,e:
				if not opts.debug: exit(e)
				raise e
			
if __name__ == '__main__':
	ClientParser().parse_args()
