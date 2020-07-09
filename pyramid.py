row = int(input("Enter number of rows: "))
num = 1
r = row + 1
print()
for i in range(1, r):
    for j in range(1, r-i):
        print(" ",end="")
    while num <= i:
        print(num,end="")
        num = num + 1
    while num-2 > 0:
        print(num-2,end="")
        num = num - 1
    num = 1
    print()