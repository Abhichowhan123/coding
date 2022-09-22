"""
# prefix max

A= [5,2,9,7,4,6,2,4,8]
max = 0
B = []
print(A)
for i in range(len(A)):
    if max<=A[i]:
        max = A[i]
        B.append(max)
    else:
        B.append(max)
print(B,"\n")

A= [5,2,9,7,4,6,2,4,8]
max = 0
B = []
print(A)
for i in range(len(A)-1,-1,-1):
    if max<=A[i]:
        max = A[i]
        B.append(max)
    else:
        B.append(max)
print(B)
B.reverse()
print(B)"""
n,p,q,r = map(int,input().split())
A = list(map(int,input().split()))

def suf(x,r):
    maxx = 0
    smax = []
    for j in range(x,len(A)):
        if maxx < r*A[j]:
            maxx = r*A[j]
            smax.append(maxx)
        else:
            smax.append(maxx)
    return max(smax)
def pre(y,p):
    maxx = 0
    pmax = []
    for i in range(y+1):
        if maxx < p*A[i]:
            maxx = p*A[i]
            pmax.append(maxx)
        else:
            pmax.append(maxx)
    return max(pmax)
min = 0

for k in range(1,len(A)-1):
    x = pre(k-1,p)+(A[k]*q) + suf(k+1,r)
    if min <x:
        min = x
print(min)