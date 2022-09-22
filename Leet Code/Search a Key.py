def search(k,l,h):
    while (l <= h):
        m = (l + h) // 2
        if k == A[m]:
            return m
        elif k > A[m]:
            l = m + 1
        else:
            h = m - 1

n = int(input())
A = list(map(int,input().split()))
for i in range(int(input())):
    k = int(input())
    l = m =0
    h = len(A)-1
    y = h+2
    e = search(k,l,h)
    if e is not None:
        print(e)
    else:
        print("-1")
