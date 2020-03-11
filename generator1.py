"""
Without generator 
"""
def sqr(num):
    for i in range(num):
        print i**2

print 10* "="+"without generator" + 10*"="
sqr(10)
print 10* "="+"with generator"
"""
Yield and genertor 
"""
def sqr(num):
    for s in range(num):
        yield s**2

mygen=sqr(10)
print type(mygen)
print mygen.next()
print mygen.next()
print mygen.next()
print mygen.next()
print mygen.next()
print mygen.next()

