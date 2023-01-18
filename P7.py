def is_prime(n):
  for i in range(2,n):
    if (n%i) == 0:
      return False
  return True

# 2 is the only even prime number, so, skipping the 2 and set counter to 1. so only odd numbers are testet
counter = 1
j = 1
while(counter != 10001):
    j += 2
    if is_prime(j):
        counter += 1

print(j)