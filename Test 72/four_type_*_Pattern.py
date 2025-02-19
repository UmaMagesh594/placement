A = int(input())
for i in range(A,0,-1):
    for j in range(i):
        print("*",end = "")
    print("  " * (A-i),end = " ")
    for j in range(i):
        print("*",end = "")
    print()
for i in range(1,A+1):
    for j in range(i):
        print("*",end = "")
    print("  " * (A-i),end = " ")
    for j in range(i):
        print("*",end = "")
    print()
