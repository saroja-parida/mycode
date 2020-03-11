def dectobin(num):
    if num > 1:
        dectobin(num//2)
    print num%2,
dectobin(100)
