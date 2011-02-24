
try:
	from osx import osx_database as database
except ImportError:
	from ini import ini_database as database
