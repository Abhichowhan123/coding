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
    merge(ar,L,R)       # merging two array or adding two array
# taking input from user
ar = []
a = int(input("enter the total no:-")) # total no for sorting

for i in range(a):
    b= int(input(":-"))
    ar.append(b)

mergesort(ar)
for k in range(len(ar)):
    print(ar[k])