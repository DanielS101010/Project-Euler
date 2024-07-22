f = open("P13 num.txt", "r")

sum = 0

for line in f:
    sum += int(line)

print(str(sum)[:10])
