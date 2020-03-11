import os
import re
import subprocess

def copy_files(spath,dest,filn):
    for root, dirs, files in os.walk(spath):
        for i in files:
            print filn
            if re.search(r'pdf',i):
                path = os.path.join(spath,i)
                iout = subprocess.Popen(['cp',path,dest],stdout=subprocess.PIPE)
                print iout
copy_files("/Users/sarojakumar.parida/Documents/test_delete/","/Users/sarojakumar.parida/Documents/delete","pdf")
