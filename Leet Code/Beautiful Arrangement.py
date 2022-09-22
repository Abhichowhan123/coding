n = 3
A = []
B = []
for i in range(1,n+1):
    A.append(i)
def perm(A,i):
    if i == len(A):
        h = 1
        v = 0
        for l in range(n):
            if (A[l]) % h == 0 or h % (A[l]) == 0:
                v += 1
                h += 1
        if v == n:
            B.append(1)
        return
    for j in range(i,len(A)):
        A[i],A[j] = A[j],A[i]
        perm(A[:],i+1)
perm(A,i=0 )
print(len(B))




