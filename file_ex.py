import traceback
def findVcs(str):
    count=0
    lst=str.split()
    for i in lst:
        if i=="vcs":
            count+=1
    return count
try:
    mycount=0
    with open("fiple_io.txt") as f:
        for l in f:
            mycount+=findVcs(l)
except IOError as e:
    print e
    traceback.print_exc()
print mycount
#print findVcs("this is vcs and vcs hello vcs")    

