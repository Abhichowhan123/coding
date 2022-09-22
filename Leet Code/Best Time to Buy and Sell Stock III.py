A = [3,3,5,0,0,3,1,4]
def left(y,t):
    m1 = 0
    b=0
    for i in range(y,t):
        for j in range(i+1,t):
            if j>i:
                b = A[j] - A[i]
                if b>0:
                    if b>m1:
                        m1 = b
    return m1
def right(o,p):
    m2 = 0
    c = 0
    for i in range(o, p):
        for j in range(i + 1, p):
            if j > i:
                c = A[j] - A[i]
                if c>0:
                    if c > m2:
                        m2 = c
    return m2
max = 0
m = 1
for m in range(1,len(A)-1):
    n=0
    if max < left(n,m)+right(m+1,len(A)):
        max = left(n,m)+right(m+1,len(A))
print(max)