f = open("P8 num.txt", "r")
num_str = f.read()

num_str = num_str.replace("\n", "")

max_product = 0
for i in range(0, 1000 - 12):
    substr = num_str[i:i + 13]
    product = 0
    for j in substr:
        if product == 0:
            product = int(j)
        else:
            product = product * int(j)

    max_product = max(max_product, product)

print(max_product)
