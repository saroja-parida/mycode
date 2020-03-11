import time

def my_decorator(fn):
    def wrapper1():
        t1=time.time()
        fn()
        t2=time.time()
        return "time taken to execute function: "+str(t2-t1)
        print("{} time taken to execute fun".format(t2-t1))
    return wrapper1
   
@my_decorator
def myFun():
    l=[]
    for i in range(1,100):
        l.append(i)
 
print myFun()
