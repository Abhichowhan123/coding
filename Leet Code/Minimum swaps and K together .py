arr = [ 2, 7, 9, 5, 8, 7, 4]
k = 6
A = []
count = j = 0
for i in range (len(arr)):
    if arr[i] <= k:
        count+=1
r = (len(arr)-count)+1
for j in range(r):
    a= count
    s = 0
    while a!=0:
        if arr[j]<=k:
            s+=1
        j+=1
        a-=1
    A.append(s)
e =max(A)
print(count-e)