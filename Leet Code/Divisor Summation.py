import math

for i in range(int(input())):
    n = int(input())
    s = d = 0
    h = n
    f = int(math.sqrt(n))
    for j in range(2,f+1):
        if n % j == 0:
            d =int( h/j)
            s= s+j+d
    print(s+1)

