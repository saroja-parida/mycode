"""
The following code will explain the supper 
and inhenritance 
"""
class A(object):
    def __init__(self):
        print "initiate class A"
    def sub(self):
        print "This is Class A sub"
class B(A):
    def __init__(self):
        A.__init__(self)
        print "override class A inside class B"
#        A.__init__(self)
#            print "override class A inside class B"
    def sub_b(self):
        print "Class B sub_b"
class C(B):
    def __init__(self):
        B.__init__(self)
        print "called class B in class A"
    def sub(self):
        print "This is class C sub and below line is from super"
        super(B, self).__init__()
obj1=C()
#print obj1
obj1.sub()
#obj1.sub_b()
