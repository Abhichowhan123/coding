"""def cal(j,n):
    b = 0
    while n != 0:
        a = n % j
        b += a
        n = int(n / j)
        if b > max:
            break
    return b
for i in range(int(input())):
    n,l,r = map(int,input().split())
    max = 99999999
    bb = 0
    if r >= n and l <= n:
        bb = n
    if l > n:
        bb = l

    else:
        for j in range(l,r):
            mini = cal(j,n)
            if max > mini:
                max = mini
                bb = j
    print(bb)
"""

def sov(n,l,r):
    bse = 0
    if r >= n >= l:
        bse = n
    if l >= n:
        bse = l

    max = 999999999999
    s = 0
    while (l < r and (n // r) < r):
        ye = n // r
        yes = n % r
        if max > (ye + yes):
            max = (ye + yes)
            bse = r
        r= n//(ye+1)
    while (l <= r):
        b = n
        s = 0
        while (1):
            if (b < l):
                s += b
                if (s < max):
                    bse = l
                    max = s
                break
            s += b % l
            b //= l
            if (s >= max):
                break
        l += 1
    return bse

for i in range(int(input())):
    n,l,r = map(int,input().split())
    print(sov(n,l,r))

"""def cal(r,b,n,max):
    while n != 0:
        a = n % r
        b += a
        n = int(n / r)
        if b>max:
            break
    return b
for i in range(int(input())):
    n,l,r = map(int,input().split())
    max = 9999999999
    b= 0
    bse = 0
    if r>n and l>n:
        bse = r
    if l<n<=r:
        bse = n
    else:
        while r!=l:
            mini = cal(r,b,n,max)
            if max > mini:
                max = mini
                bse = r
            if max ==1:
                break
            r -= 1
    print(bse)"""

""" """