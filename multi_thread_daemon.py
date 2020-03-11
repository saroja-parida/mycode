import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG,format='(%(threadName)-10s) %(message)s',)

def myfun_d():
    logging.debug('Starting')
    time.sleep(2)
    logging.debug('Exiting')

d = threading.Thread(name='daemon', target=myfun_d)
d.setDaemon(True)

def myfun_nd():
    logging.debug('Starting')
    logging.debug('Exiting')

t = threading.Thread(name='non-daemon', target=myfun_nd)

d.start()
t.start()
