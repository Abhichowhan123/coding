A =[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

for i in range(len(A)-1):
    j =i+1
    k =i
    while j>0:
        if A[j]<A[k]:
            A[j],A[k]=A[k],A[j]
        j-=1
        k-=1
print(A)