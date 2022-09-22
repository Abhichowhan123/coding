arr = [1,2,3,4,5]
k = 4
x = 3
l,r = 0,len(arr)-k
while l<r:
    m = (l+r)//2
    if x-arr[m]>arr[m+k]-x:
        l=m+1
    else:
        r= m
print(arr[l:l+k])