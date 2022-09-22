def first(k,l,h):
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
    return (-1)
def last(k,l,h):
    while (l <= h):
        m = (l + h) // 2
        if k > A[m]:
            l = m + 1
        elif k< A[m]:
            h = m - 1
        else:
            if m == len(A)-1:
                return m
            elif A[m + 1] != k:
                return m
            else:
                l = m + 1
    return (-1)
n = int(input())
A = list(map(int,input().split()))
for i in range(int(input())):
    k = int(input())
    l = 0
    h = len(A) - 1

    w = first(k,l ,h )
    d = last(k, l, h)
    if w == -1 and d == -1:
        print("0")
    elif w>=0:
        print((d-w)+1)
