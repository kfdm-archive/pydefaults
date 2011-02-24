from ConfigParser import ConfigParser,NoOptionError,NoSectionError,Error

class ini_database:
	__file = None
	__config = None
	def __init__(self,file):
		self.__file = file
		self.__config = ConfigParser()
		try: self.__config.readfp(open(self.__file))
		except IOError,e:
			self.__config.write(open(self.__file,'w'))
			raise Error('No config file found.  Writing defaults to'+file)
	def read(self,domain=None,key=None):
		if domain is None:
			hash = {}
			for domain in self.domains():
				hash[domain] = self.read(domain)
			return hash
		
		# Domain Only
		if not self.__config.has_section(domain):
			raise Error('Domain %s does not exist'%domain)
		if key is None:
			return self.__config.items(domain)
		
		if not self.__config.has_option(domain, key):
			raise Error('Domain (%s,%s) does not exist'%(domain,key))
		return self.__config.get(domain,key)
	def write(self,domain,key,value):
		if not self.__config.has_section(domain):
			self.__config.add_section(domain)
		self.__config.set(domain, key, value)
		self.__config.write(open(self.__file,'w'))
		return value
	def delete(self,domain,key=None):
		if not self.__config.has_section(domain):
			return ''
		if key and self.__config.has_option(domain, key):
			self.__config.remove_option(domain, key)
		if len(self.__config.items(domain)) == 0:
			self.__config.remove_section(domain)
		if not key:
			self.__config.remove_section(domain)
		self.__config.write(open(self.__file,'w'))
	def rename(self,domain,old_key,new_key):
		value = self.read(domain, old_key)
		self.write(domain, new_key, value)
		self.delete(domain, old_key)
	def domains(self):
		return self.__config.sections()
