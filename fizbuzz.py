def fizbuzz(n):
    list1=[(i,not i%3, not i%5) for i in range (1,n)]
    print(list1)
    message={
        (True,True):"fizbuzz",
        (True,False):"buzz",
        (False,True):"fizz",
        (False,False):""
    }
    list2=[message[(a,b)] or i for i,a,b in list1]
    for j in list2:
        print(j,)

fizbuzz(20)