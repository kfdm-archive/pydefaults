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
	
	domains
'''
		OptionParser.__init__(self,usage=usage)
		self.add_option("-f","--file",help="Filename",
						dest='file',default='~/.pydefaults')
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
				os.system('%s %s'%(os.environ['EDITOR'],opts.file))
			exit()
		if len(args) < 1:
			exit(self.print_help())
		
		db = defaults(opts.file)
		if opts.debug:
			db._defaults__debug = True
		cmds = {
			'read':(db.read,0,2),
			'write':(db.write,3,3),
			'rename':(db.rename,3,3),
			'delete':(db.delete,1,2),
			'domains':(db.domains,0,0),
		}
		if not cmds.has_key(args[0]):
			self.error('Unknown command %s'%args[0])
		func,min,max = cmds.get(args[0])
		args = args[1:] # Pop off the command
		if len(args) < min or len(args) > max:
			return self.error('Invalid Arguments')
		try:
			print func(*args)
		except Error,e:
			if not opts.debug:
				exit(e)
			raise e
			
if __name__ == '__main__':
	ClientParser().parse_args()
