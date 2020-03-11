def genfib(num):
    a=1
    b=1
    for i in range(num):
        yield a
#        t = a
#        a = b
#        b = t+b
        a,b = b, a+b
for s in genfib(10):
    print s
