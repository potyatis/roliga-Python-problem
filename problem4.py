prod = []
for i in range(100, 1000):
    for j in range(100, 1000):
        prod.append(i*j)
pal = []
for i in prod:
    j = str(i)[::-1]
    if j == str(i):
        pal.append(i)
a = 0
for i in pal:
    if i > a:
        a = i
print(a)