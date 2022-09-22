
for k in range(int(input("no of input\n"))):
    a,b = map(int,input("two no for LCM\n").split())
    s = max(a,b)
    for i in range(s, a * b):
        if i % a == 0 and i % b == 0:
            print(i)
            break