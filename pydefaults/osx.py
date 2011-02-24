from Foundation import *
standardUserDefaults = NSUserDefaults.standardUserDefaults()
persistentDomains = standardUserDefaults.persistentDomainNames()
persistentDomains.objectAtIndex_(14)
aDomain = standardUserDefaults.persistentDomainForName_(persistentDomains[14])
aDomain.keys()

class osx_database:
	__domain__ = None
	__config__ = None
	def __init__(self,domain):
		self.__domain__ = domain
		defaults = NSUserDefaults.standardUserDefaults()
		self.__config__ = defaults.persistentDomainForName_(domain)
		if self.__config__ is None: self.__config__ = {}
	def read(self,key,default=None):
		return self.__config__.get(key,default)
	def write(self,key,value):
		self.__config__.addObject_forKey_(key,value)
	def __getitem__(self,key):
		return self.read(key)
