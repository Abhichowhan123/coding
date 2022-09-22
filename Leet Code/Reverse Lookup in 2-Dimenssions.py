# A=[[1,1]
#    ,[1,1]]
A= [[1,2,3],
    [1,2,3],
    [1,2,3],
    [1,2,3]]
sum = 0
for i in range(len(A)):
    for j in range(len(A[0])):
        sum+= A[i][j]* (i+1)*(j+1)*(len(A)-i)*(len(A[0])-j)
print(sum)