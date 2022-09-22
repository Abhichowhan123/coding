t = int(input())
for i in range(t):
    a,b = map(int,input().split())
    c = a*b
    if (a>1000):
        d =c - (c * (10/100))
        print(float(d))
    else:
        print(float(c))

