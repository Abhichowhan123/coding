# A = [[3, 0, 1],
#       [5, 6, 3],
#       [1, 0, 3]]
A = [[2,0,1],
     [1,0,1],
     [0,3,0]]

for i in range(len(A)):
      b = 0
      for j in range(len(A)):
            b += A[i][j]
            A[i][j] = b
print(A)
for k in range(len(A)):
      c=0
      for l in range(len(A)):
            c+=A[l][k]
            A[l][k] = c
print(A)