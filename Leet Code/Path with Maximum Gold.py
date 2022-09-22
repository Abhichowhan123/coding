grid = [[0,6,0],[5,8,7],[0,9,0]]
m = [[False]*len(grid[0])]*len(grid)

def rec(i,j):



ans = 0
for i in range(len(grid[0])):
    for j in range(len(grid)):
        ans = max(ans,rec(i,j))