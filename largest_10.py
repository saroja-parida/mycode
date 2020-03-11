list1 = ["1","10","3","22","23","4","2","200"]
list2 = [int(x) for x in list1]

#list2.sort()
#print list2
print sorted({3,233,2,1,23,78})
print sorted({"saroj","abc","ban","aam","ankur","ziat","mant"})

def bubble_sort(l1):
    for i in range(len(l1)):
        for j in range(len(l1)-1-i):
            if l1[j] > l1[j+1]:
                l1[j],l1[j+1] = l1[j+1],l1[j] #swap

bubble_sort(list1)
print list1


