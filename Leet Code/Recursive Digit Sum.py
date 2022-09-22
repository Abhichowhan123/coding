def rec(n,b):
    if n == 0:
        if b<10:
            return print(b)
        else:
            return rec(b,0)

    b = int(b + n%10)
    n = int(n/10)
    rec(n,b)
n = 123
k = 3
b  = a = 0
for i in range(k):
    a= a+n%10
    n = int(n/10)
rec(a*k,b)