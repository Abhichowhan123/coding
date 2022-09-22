mat = [[1,2,3],
       [4,5,6],
       [7,8,9]]
n = len(mat[0])
m= len(mat)
row = 0
col = 0
A = []
for i in range(n*m):
    A.append(mat[row][col])
    if (row+col)%2==0:
        if col ==n-1:
            row+=1
        elif row==0:
            col+=1
        else:
            row-=1
            col+=1
    else:
        if row ==(m-1):
            col+=1
        elif col == 0:
            row+=1
        else:
            row+=1
            col-=1
print(A)
