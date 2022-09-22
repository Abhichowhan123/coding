
def first(m,k,h):
    if m == 0:
        return m
    elif A[m - 1] != k:
        return m
    else:
        h = m - 1
        return h
def search(k,l,h):
    while (l <= h):
        m = (l + h) // 2
        if k > A[m]:
            l = m + 1
        elif k< A[m]:
            h = m - 1
        else:
            if m == 0:
                return m
            elif A[m - 1] != k:
                return m
            else:
                h = m - 1
n = int(input())
A = list(map(int,input().split()))
w = search(k=1, l=0, h=len(A) - 1)
if w:
    print(w+1)
else:
    print("-1")
