#Find latest files
import os
import datetime
import time

def find_latest(sdir):
    for root,dirs,files in os.walk(sdir):
        for i in files:
            #the get ctime returns in seconds 
            date = os.path.getctime(i)
            #To print in proper time format use the ctime
            print time.ctime(date)
            print datetime.time(int(date))
dirname = input("Enter the directory name :") 
find_latest(\"dirname\")
