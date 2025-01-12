import math


b = 1000000000000
a = math.floor(b*0.70710678118)
while b < 10000000000000:
    if (a*(a-1))*2 == (b*(b-1)):
        print(a)
        print(b)
        b += 1
    elif (a*(a-1))*2 < (b*(b-1)):
        a += 1
        continue
    else:
        b += 1
        continue
print("vafan")
