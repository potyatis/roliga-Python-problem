primes = [2]
number = 2
while len(primes) < 10001:
    number += 1
    for prime in primes:
        if number % prime == 0:
            break
        elif prime < number **(1/2):
            continue
        else:
            primes.append(number)
            break
print(primes[-1])