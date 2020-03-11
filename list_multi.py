var = ([1,2,3],[3,4,5],[1,0,-1])

def sumlist(*args):
    sum_l=[]
    for a in args:
        sum_each=0
        for b in a:
           sum_each+=b
        sum_l.append(sum_each)
    return sum_l

tst=sumlist([1,2,3],[3,4,5],[1,0,-1])
print tst


