import math


def prime_number(num):
    max_num = int(math.sqrt(num))

    if num == 1:
        return False
    elif num > 1:
        for j in range(2, max_num + 1):
            if num % j == 0:
                return False
        return True


number = 2000000
sum_prime = 2
for i in range(3, number, 2):
    if prime_number(i):
        sum_prime += i

print(sum_prime)

# optimization with Sieve of Eratosthenes

import numpy as np


def sieve_of_eratosthenes(n):
    is_prime = np.ones(n, dtype=bool)
    is_prime[0:2] = False  # 0 and 1 are not primes
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            is_prime[i * i:n:i] = False
    return is_prime


number = 2000000
primes = sieve_of_eratosthenes(number)
sum_prime = np.sum(np.nonzero(primes)[0])
print(sum_prime)
