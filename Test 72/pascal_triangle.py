A = int(input())
print("** Printing the pattern... **")
for i in range(A):
    num = 1
    if A == 3:
        print(" " * (A-i),end = "")
    else:
        print(" " * (A-i-1),end = "")
    for j in range(i+1):
        if j == i:
            print(num,end = " ")
        else:
            print(num,end = " ")
        num = num * (i-j) // (j+1)
    print()
