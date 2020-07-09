t = True
Case = int(input("Enter total number of cases: "))
if Case <= 0 or Case >= 10:
    print("Please enter a number within 0 to 10")
    Case = input("Enter total number of cases: ")
c = Case + 1
for i in range(1, c):
    num = int(input("Enter Number: "))
    n = num+1
    for j in range(0, n):
        names = input("Enter Names: ")
    for k in range(0, n):
        if names[k] != names[k+1] and t == True:
            t = True
        else:
            t = False
    if t == True:
        print(f"Case #{i}: Yes")
    if t == False:
        print(f"Case #{i}: No")
