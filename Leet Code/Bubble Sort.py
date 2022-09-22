A = [4, 1, 3, 9, 7]
for i in range(len(A)):
    for j in range((len(A)-1)-i):
        if A[j]>A[j+1]:
            A[j],A[j+1]=A[j+1],A[j]

print(A)