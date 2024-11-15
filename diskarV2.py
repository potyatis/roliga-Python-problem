import math
for a in range(100000000000, 1000000000000):
    b = math.floor(a*(2**0.5))
    if b*(b-1) == 2*a*(a-1):
        print(a)
        print(b)
print("vafan")