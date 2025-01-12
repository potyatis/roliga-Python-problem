
a = 600851475143
i = 2
while i < a:
    if (a / i) % 1 == 0:
        a = a / i
    else:
        i += 1
print(a)
