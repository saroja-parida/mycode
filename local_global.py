al=[1,2,3]
a=4

def myfun():
    a=6
    al=[2,3,4]
    print a
    print al
 
print a
print al
myfun()

print "==" * 50
def myfun1():
    global a
    a=6
    al=[2,3,4]
    print a
    print al
print a
print al
myfun()
