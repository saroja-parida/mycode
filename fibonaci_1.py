# print("#===============================")
# print("fibonaci sequence starting from zero and count till a number")
# print "#=========================================="
# def fib1(n):
#     a,b = 0,1
#     count = 0
#     print(0)
#     while (count < n-1):
#         a , b = b, a+b
#         print (a)
#         count+=1
# print(fib1(10))
# print("#===============================")
# print("fibonaci sequence till a number reached")
# print("#==========================================")
#
# def fib2(n):
#     a,b = 0,1
#     print(0)
#     while (b < n):
#         a,b=b,a+b
#         print(a)
# print(fib2(90))
# print ("#===============================")
# print ("fibonaci sequence with recurrson till a number reached")
# print ("#==========================================")
#
# def fib3():
#     a,b=0,1
#     while True:
#         a,b=b,a+b
#         yield a
#
# f=fib3()
# print (f.next())
# print (f.next())
# print (f.next())
# print (f.next())

def fibr(n):
    if n==0:
        print(0)
    if n==1:
        print(1)
    else:
        print(fibr(n-1)+fibr(n-2))

fibr(10)