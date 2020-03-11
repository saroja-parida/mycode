#Thread naming 
import threading
import time
def worker():
    print threading.currentThread().getName(),"starting"
    time.sleep(2)
    print threading.currentThread().getName(),"exiting"
def myfun():
    print threading.currentThread().getName(),"starting"
    time.sleep(3)
    print threading.currentThread().getName(),"exiting"

t=threading.Thread(name="my first thread",target=worker)
w=threading.Thread(name="my second thread",target=myfun)
a=threading.Thread(target=worker)


t.start()
w.start()
a.start()
