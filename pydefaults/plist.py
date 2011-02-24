import plistlib
import os

class plist_database:
	__file__ = None
	__config__ = None
	def __init__(self,domain):
		self.__domain__ = domain
		self.__dir__ = os.path.join(os.path.expanduser('~'),'.defaults')
		self.__file__ = os.path.join(self.__dir__,domain)
		if os.path.exists(self.__file__):
			self.__config__ = plistlib.readPlist(self.__file__)
		else:
			self.__config__ = {}
	def _write(self):
		dir = os.path.dirname(self.__file__)
		if not os.path.exists(dir): os.mkdir(dir)
		plistlib.writePlist(self.__config__,self.__file__)		
	def read(self,key,default=None):
		return self.__config__.get(key,default)
	def write(self,key,value):
		self.__config__[key] = value
		self._write()
	def delete(self,key):
		self.__config__[key] = None
		self._write()
	def rename(self,old_key,new_key):
		self.__config__[new_key] = self.__config__[old_key]
		self._write()
