"""
Get prime numbers from a list of numbers
given by the user
"""
def prime_list(lst):
    primes=[]
    for i in lst:
        if str(i).isdigit():
            if isPrime(i):
                primes.append(i)
        else:
            print("{} is not a valid number".format(i))
            continue
    return primes

def isPrime(n):
    if n==2:
        return True
    for i in range(3,n-1):
        if n%i==0:
            return False
    return True
"""
print isPrime("sp")
print isPrime(3)
print isPrime(11)
"""
list1=[3,"saroj",12,11,23,12,14,21,101,121]
print list1
print prime_list(list1)
