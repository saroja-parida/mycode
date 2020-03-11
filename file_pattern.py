"""
Open files in a given directory 
and print lines with a given pattern
use generator
"""
import traceback
class files:
    def __init__(self):
        print"The class is initiated"
        self.patt=""
        self.filen=""
    def searchP(self,patt,filen):
        try:
           if self.patt in self.filen:
                    return True
        except:
            print"There is some issue"
            traceback.print_exc()

obj=files()
try:
    count=0
    with open("test.txt","r") as f:
        for line in f.readlines():
            if obj.searchP("temp",line):
                count+=1
    print count 
except IOError as e:
    print"my exception raised"
