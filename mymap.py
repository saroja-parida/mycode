#Write your own mymap() function which works exactly like Python's built-in function
def myMap(fn,c):
    NewC=[]
    for i in c:
        NewC.append(fn(i))
    return NewC
l=[1,2,3,4]
print myMap(lambda x:x*2,l)
