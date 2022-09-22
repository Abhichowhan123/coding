def merge(ar , L , R ):
    len_L = len(L)
    len_R = len(R)
    i = j = k = 0
    while i < len_L and j < len_R:   # checking the length of array is not less then i value
        if L[i] <= R[j]:
            ar[k] = L[i]
            i += 1
        else:
            ar[k] = R[j]
            j += 1
        k += 1
    while i < len_L:
        ar[k] = L[i]
        i += 1
        k+=1
    while j<len_R:
        ar[k] = R[j]
        j += 1
        k+=1
def mergesort(ar):       # recursion
    if len(ar) <= 1:
        return ar
    mid = len(ar)//2     # dividing into tow array
    L = ar[:mid]         # left array
    R = ar[mid:]         # right array
    mergesort(L)
    mergesort(R)
    merge(ar,L,R)
for i in range(int(input())):
    n,k=map(int,input().split())
    B = []
    ar = list(map(int,input().split()))
    mergesort(ar)
    while n!=0 :
        n-=1
        B.append(ar[n])
    count = 0
    a= len(B)
    k= k-1
    while a!=0:
        a -= 1
        if B[k]<=B[a]:
            count+=1
    print(count)
