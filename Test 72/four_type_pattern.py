a=int(input())
for i in range(1,a+1):
    print(" "*(a-i),end="")
    print("*"*i,end=" ")
    start_char=64+i
    for j in range(1,i+1):
        print(chr(start_char),end="")
        start_char+=1
        
    print()
dup=a
for i in range(a,0,-1):
    print(" "*(a-i),end="")
    for j in range(1,i+1):
        print(dup,end="")
        dup-=1
    dup=a
    print(" ",end="")
    num=1+(a-i)*2
    for j in range(i):
        print(num,end="")
        num+=2
    print()
