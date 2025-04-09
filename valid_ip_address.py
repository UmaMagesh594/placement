def valid(x):
    return x == str(int(x)) and int(x) <= 255
s = input()
co = 0
for i in range(1,len(s)):
    for j in range(i+1,len(s)):
        for k in range(j+1,len(s)):
            a = s[:i]
            b = s[i:j]
            c = s[j:k]
            d = s[k:]
            if valid(a) and valid(b) and valid(c) and valid(d):
                co += 1
                # print(a+"."+b+"."+c+"."+d)
print(co)
