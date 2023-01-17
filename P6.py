sumOfSquared = 0
squaredSum = 0

#Easy Solution
for i in range(101):
    sumOfSquared += i**2
    squaredSum += i

squaredSum = squaredSum**2
print(squaredSum - sumOfSquared)

#fast solution
squaredSum = (100*(100+1)/2)**2
sumOfSquared = (1/6)*(2*100**3 + 3*100 **2 + 100)
print(squaredSum - sumOfSquared)