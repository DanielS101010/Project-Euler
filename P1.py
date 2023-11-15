import math
# easy but slower solutiom
target = 1000
sum = 0
for i in range(target):
    if (i % 3 == 0 or i % 5 == 0):
        sum += i
print(sum)

# better solution
def sumDivisibleBy(n):
    p = math.floor(target / n)
    return n * (p * (p + 1)) / 2

print(sumDivisibleBy(3) + sumDivisibleBy(5) - sumDivisibleBy(15))
