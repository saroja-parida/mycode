"""
Move files which are two days old to specified location
"""
import os
import datetime as dt
import shutil
import string

nw=dt.datetime.now()
twodold=nw.dt.timedelta(hours=48)
def move_f(path):
    for dpath,dirn,filen in os.walk(path):
        for fname in filen:
            file_d=os.path.join(dpath,fname)
            stat=os.stat(file_d).st_ctime
            mod_d=dt.datetime.fromtimestamp(stat)
            if mod_d < twodold:
                print("The file{} is two days old, archiving it".format(fname))
                destdir=string.replace(str(mod_d),' ','_')
                print("creating new dir..{}/{}".format(dpath,destdir))
                os.mkdir(dpath +"/"+ destdir)
                print("Copy file {} to destinatin {}".format(fname,os.path.join(dpath,destdir)))
                shutil.copy(file_d,os.path.join(dpath,os.path.join(dpath,destdir)))
            
move_f("/Users/sarojakumar.parida/Downloads/check-in")            
