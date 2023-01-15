import math
i = 2
n = 600851475143
n_sqrt = math.sqrt(n)
faktoren = []
while i <= n_sqrt:
    if n%i == 0:
        faktoren.append(i)
        n = n/i

    i = i+1

print(faktoren)