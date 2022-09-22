matrix = [[-5]]
k = 1
A  = []
for i in range(len(matrix)):
    A+=matrix[i]
A = sorted(A)
print(A)
print(A[k-1])
