"""
This class has methods to sort and merge 
"""
class myclass(object):
    """
    merge two sorted listsfunction
    """
    def merge_l(self,list1,list2):
        list_m=[]
        while list1 and list2:
            if list1[-1]>list2[-1]:
                list_m.append(list1.pop())
            else:
                list_m.append(list2.pop())
        list_m+=(list1+list2)[::-1]
        return list_m

class myclass2(myclass):
    """
    sorting a list
    """
    def sort_l(self,list1):
        print(list1)
        for i in range(1,len(list1)):
            j=i
            while j>0 and list1[j] < list1[j-1]:
                list1[j], list1[j-1] = list1[j-1], list1[j]
                j=j-1
        return list1    

obj=myclass2()
print(obj.merge_l([1,2,3,5],[4,6,7,8]))
l=[10,3,11,2,12,1]
print(obj.sort_l(l))
