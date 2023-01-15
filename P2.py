list = [1, 2]
sum = 0
while list[len(list)-1] <= 4000000:
    list.append(list[len(list) - 2] + list[len(list)-1])

for i in list:
    if i % 2 == 0:
        sum += i

print(sum)