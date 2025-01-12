import math


b = 10
a = 0.5 + math.sqrt(0.25+(b*(b-1)/2))
for i in range(10000000000000):
    b += 1
    a = 0.5 + math.sqrt(0.25+(b*(b-1)/2))
    if a % 1 == 0:
        print(a)
        print("woho", b)
print("vafan")
