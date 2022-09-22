def search(k,l,h):
    if k <=A[l]:
        return l
    elif k>A[h]:
        return h+1
    while (l <= h):
        m = (l + h) // 2
        if A[m]>=k and k<=A[m+1] :
            return m
        elif k > A[m]:
            l = m + 1
        else:
            h = m - 1
n = int(input())
A = list(map(int,input().split()))
for i in range(int(input())):
    print(search(k = int(input()),l =0,h = len(A)-1))