x = 20
bool = False
while(bool == False):
    bool = True
    print(x)
    for i in range(11,20 + 1): #if its divible through 11 to 20, then it is also divible through 1 to 10
        if x%i != 0:
            bool = False
    x += 20
print(x)