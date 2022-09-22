grid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]
C,R = len(grid[0]),len(grid)
mat = [[0 for x in range (C)] for y in range(R)]

def Unique_Paths(i,j,count,total_count,mat):
    a = 0
    if i >0 and j >0 and i < len(grid) - 1 and j < len(grid)-1:
        return
    elif grid[i][j]==2 and count==0:
        total_count+=1
        return
    mat[i][j] = -1
    if i+1<len(grid):
        if grid[i + 1][j] == 0 and mat[i + 1][j] == 0 :
            Unique_Paths(i + 1, j, count - 1, total_count, mat)
    elif j  < len(grid[0])-1:
        if grid[i][j + 1] == 0 and mat[i][j + 1] == 0:
            Unique_Paths(i, j + 1, count - 1, total_count, mat)
    elif i - 1 >0:
        if grid[i - 1][j] == 0 and mat[i - 1][j] == 0:
            Unique_Paths(i - 1, j, count - 1, total_count, mat)
    elif j - 1 >0:
        if grid[i][j - 1] == 0 and mat[i][j - 1] == 0:
            Unique_Paths(i, j - 1, count - 1, total_count, mat)

count = a = b=total_count =0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j]==0:
            count+=1
        if  grid[i][j]==1:
            a = i
            b=j
Unique_Paths(a,b,count,total_count,mat)



























