def pivot(l,h):
    while l<=h:
        m = (l+h)//2
        if L[m] <= L[len(L) - 1]:
            h = m - 1
        else:
            if L[m] > L[m + 1]:
                return m
            else:
                l = m + 1
    return 555
def rotated1(k):
    l =0
    h = len(L)-1
    while l<=h:
        m = (l+h)//2
        if L[m]==k:
            return m
        elif k<L[m]:
            h=m-1
        elif k>L[m]:
            l = m+1
    return -44
def rotated(p,k):
    if k<= L[len(L)-1]:
        l = p+1
        h = len(L)-1
        while (l <= h):
            m = (l + h) // 2
            if L[m] == k:
                return m
            if k > L[p + 1]:
                l = m + 1
            if k < L[len(L) - 1]:
                h = m - 1
    else:
        l=0
        h = p
        while(l<=h):
            m = (l+h)//2
            if L[m]==k:
                return m
            if k<L[m]:
                h = m-1
            elif k>L[m]:
                l = m+1
    return -44
# # n = 7
# L = [4,5,6,7,0,1,2]
# L = [0,1,2,4,5,6,7 ]
# k = 5
# p = int(pivot(l=0, h=len(L) - 1))
# if p==555:
#     r =int(rotated1(k))
# else:
#     r = int(rotated(p, k))
# if r!= (-44):
#     print(r)
# else:
#     print("-1")
n = int(input())
L = list(map(int,input().split()))
for i in range(int(input())):
    k = int(input())
    p = int(pivot(l=0, h=len(L) - 1))
    if p == 555:
        r = int(rotated1(k))
    else:
        r = int(rotated(p, k))
    if r != (-44):
        print(r)
    else:
        print("-1")