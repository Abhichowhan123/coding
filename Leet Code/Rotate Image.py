# transposeing the matrix
A = [[1,2,3],
     [4,5,6],
     [7,8,9]]

for i in range(len(A)):
    for j in range(i):
        t = A[i][j]
        A[i][j]=A[j][i]
        A[j][i] = t
#   reversing array
for i in range(len(A)):
    A[i].reverse()
#   printing the matrix
for i in range(len(A)):
    print(A[i])
