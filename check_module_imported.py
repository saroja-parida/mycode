#!/usr/bin/python
try:
	import sys
	import xlrd
	from pprint import pprint as p
except ImportError as e:
	print ("Module is not imported",e)
s=raw_input("Enter module name :" )
print "{} is the type of sys.modules".format(type(sys.modules))
#p(sys.modules)
try:
	if s in sys.modules:
    		print "{} module is imported".format(s)
	else:	
		print "{} module is not imported here".format(s)
except:
    		print "{} module is not imported".format(s)
