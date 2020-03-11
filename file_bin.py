# File has binary numbers
# Find out the line with largest binary number

import os.path

def findOne(ln):
    count =0
    for i in ln:
        if i=='1':
            count+=1
    return count
#print findOne([1,1,1,1,1,1,0,0])
list1=[]
if os.path.exists("bin.txt"):
    with open("bin.txt","r") as f:
        for ln in f.readlines():
#           print ln,
            s=[x for x in ln]
#           print s,
            list1.append(findOne(s))
            print ("Total number of 1 in '{}' is {}".format(ln,findOne(s)))
print list1    
test=reduce(lambda x,y:x if x >y else y,list1)
print test
