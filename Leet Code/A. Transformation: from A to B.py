import math
a= 100
A = []
def transform(b,n):
    c = isinstance(b,float)
    if c:
        return
    if b==a:
        return
    if b%2 ==0:
        b/=2
        b = math.ceil(b)
        A.append(b)
    else:
        b/=2
    transform(b,n+1)
    b = (b-1)/10
    if b % 2 == 0:
        b = math.ceil(b)
        A.append(b)
    else:
        b =b
    transform(b,n)
transform(b=40021,n = 0)
print(A)