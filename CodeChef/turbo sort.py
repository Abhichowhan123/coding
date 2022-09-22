def bubble_sort(a):
    for j  in range (len(a)):
        for i in range(len(a)):
            if i < len(a)-1 :
                if a[i]>a[i+1]:
                    a[i],a[i+1]=a[i+1],a[i]
                else:
                    i+=1
arr = []
n = int(input())
for i in range(n):
    m = int(input())
    arr.append(m)
bubble_sort(arr)
for k in range(len(arr)):
    print(arr[k])
"""
i = 0
a = [0,5,6,4,1,155]
for j  in range (len(a)):
    for i in range(len(a)):
        if i < len(a)-1 :
            if a[i]>a[i+1]:
                a[i],a[i+1]=a[i+1],a[i]
            else:
                i+=1
print(a)
"""