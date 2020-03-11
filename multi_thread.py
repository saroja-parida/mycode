#simple thread programming 
import threading 

def worker(num):
    print("worker number {}".format(num))
    return
for i in range(2):
    t=threading.Thread(target=worker,args=(i,))
    t.start()
