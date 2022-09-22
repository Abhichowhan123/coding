"""def chec(a,b):
    c = ""
    d = ""
    for l in range(0,len(a)):
        for m in range(0,len(b)):
            if (a[l]==b[m]):
                c.join(a[l])
                d.join(b[m])
    print(c,d)"""

def even(n):
    a = []
    b = []
    c = ""
    d = ""
    A = []
    B = []
    w = int(len(n)/2)
    for j in range(0,len(n)-w):
        a.append(n[j])
    for k in range(w,len(n)):
        b.append(n[k])

    for l in range(0, len(a)):
        for m in range(0, len(b)):
            if (a[l] == b[m]):
                A.append(a[l])
                B.append(b[m])
            else:
                A.append(a[l])
                B.append(b[m])

    e = c.join(A)
    f = d.join(B)
    print(e,f)


def odd(n):
    pass
#t = int(input("number of time"))
#for i in range(t):
n = list(input())
if (len(n)%2 == 0):
    even(n)
else:
    odd(n)