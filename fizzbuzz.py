from random import *
lis = []
for x in range (100):
    a = randint(1,100)
    lis.append(a)
print (lis)
for y in range (0,100):
    b = lis[y]
    print (b)
    if b%3 == 0 and b%5 != 0:
        print ("fizz")
    elif b%3 != 0 and b%5 == 0:
        print ("buzz")
    elif b%3 == 0 and b%5 == 0:
        print ("fizzbuzz")
    else:
        print (b)
    
