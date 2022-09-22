import math

for j in range(int(input())):
    n  = int(input())

    w= int(math.log(n,2))
    k= math.pow(2,w)
    a = int((n-k)+1)
    b = int(k//2)
    print(max(a,b))