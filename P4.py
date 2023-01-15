palindrome  = []
for i in range(999,2, -1):
    for x in range(999, 2, -1):
        num = i*x
        num = str(num)
        if (num == num[::-1]):
            num = int(num)
            palindrome.append(num)


palindrome.sort()
print(palindrome[-1])
