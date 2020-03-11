#!/usr/bin/python

l=[10,2,30,4,51]
for a,b in enumerate(l):
        if b%2==0:
	  print "{} is the index of {}".format(a,b)
