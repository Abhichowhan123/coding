pos = -1
def binary_search(ar,r):
    low = 0
    upp = len(ar)-1
    while low < upp:
        mid = (low + upp)//2
        if ar[mid] == r:
            print("found at ",mid)
            break
        else:
            if ar[mid] < r:
                low = mid
            else:
                upp = mid

def merge(ar, left, right):
    len_left = len(left)
    len_right = len(right)
    i = j = k = 0

    while i < len_left and j < len_right:
        if left[i] <= right[j]:
            ar[k] = left[i]
            i += 1
        else:
            ar[k] = right[j]
            j += 1
        k += 1

    while i < len_left:
        ar[k] = left[i]
        i += 1
        k += 1

    while j < len_right:
        ar[k] = right[j]
        j += 1
        k += 1

def mergesort(ar):
    if len(ar) <= 1:
        return ar
    mid = len(ar)//2

    left = ar[:mid]
    right = ar[mid:]

    mergesort(left)
    mergesort(right)

    merge(ar, left, right)


# main
# taking random input and sorting for binary search
ar = []
n = int(input("enter the total no for array:-"))
for i in range(n):
    m = int(input(":-"))
    ar.append(m)
print(ar)
# shorting the  array by using mergesort algorithm
mergesort(ar)
print(ar)

r = int(input("enter the number for search:-"))

binary_search(ar,r)
print("not found")
