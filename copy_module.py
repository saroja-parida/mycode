"""
The following code demonstrates copy and deep copy
functionalites
"""
import copy
class copy_c:
    def __init__(self):
        print("The class object initiated .......")
    @classmethod
    def copy_f(self):
        print "=="*25 +"Shallow copy"+"=="*20
        a=[1,2,3]
        print("{} is id of a".format(id(a)))
        print a
        b=copy.copy(a)
        print("{} is id of b".format(id(b)))
        print b
print copy_c.copy_f()
