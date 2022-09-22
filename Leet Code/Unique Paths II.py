obstacleGrid = [[0,0,0],
                [0,1,0],
                [0,0,0]]
m  =len(obstacleGrid)
n = len(obstacleGrid[0])
def Unique(i,j,obstacleGrid,m,n,count):
    if i==m-1 and j==n-1:
        return 1
    if obstacleGrid[i][j]==1 and i>m-1 and j>n-1 :
        return
    if j>n-1:
        count+=Unique(i+1, j, obstacleGrid, m, n,count)
    elif i>m-1:
        count += Unique(i, j + 1, obstacleGrid, m, n, count)
    else:
        count += Unique(i + 1, j, obstacleGrid, m, n, count)
        count += Unique(i, j + 1, obstacleGrid, m, n, count)
    # i-=1
    # j-=1
count = 0
Unique(0, 0, obstacleGrid,m,n,count)