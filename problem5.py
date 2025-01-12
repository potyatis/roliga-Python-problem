factors = []
a = 1
g = 20
for i in range(2, 21):
    if a % i != 0:
        if i ** 4 <= g:
            a *= i**4
        elif i ** 3 <= g:
            a *= i ** 3
        elif i ** 2 <= g:
            a *= i ** 2
        else:
            a *= i
    print(a)