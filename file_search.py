def file_s():
    f=open("test1.txt","r")
    count = 0
    for line in f:
        if "saroj" in line:
            count+=1
    print("The name 'saroj' is repeted  =%d times "%(count))
s=0
if "saroj" in open("test1.txt").read():
   s+=1
print s   

print open("test1.txt").read().find('saroj')
file_s()

list1 =["saroj","sp","saroj11","saroj1234","saroj"]
def findl(lis):
    count=0
    match="saroj\w+"
    for i in lis:
        if i == match:
            print "matched"
            count+=1
    return count

print findl(list1)
