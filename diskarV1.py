import math


b = 10
a = math.floor(b*0.70710678118)
while b < 10000000000000:
    if (a*(a-1))*2 == (b*(b-1)):
        for i in range (10000):
            print("woho", a)
            print("woho", b)
        b += 1
    elif (a*(a-1))*2 < (b*(b-1)):
        a += 1
        continue
    else:
        print(b)
        b += 1
        continue
print("vafan")
