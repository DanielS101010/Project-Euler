def is_prime(n):
  for i in range(2,n):
    if (n%i) == 0:
      return False
  return True

counter = 0
j = 1
while(counter != 10001):
    j += 1
    if is_prime(j):
        counter += 1

print(j)