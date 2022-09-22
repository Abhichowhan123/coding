grid = [[1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]]
A = []
for row in range(len(grid)):
    for col in range(len(grid[0])):
        if row == 0 and col!=0:
            grid[row][col] += grid[row][col - 1]
        elif col == 0 and row!=0:
            grid[row][col] += grid[row - 1][col]
        elif col!=0 and row != 0:
            grid[row][col] += min(grid[row-1][col],grid[row ][col-1])
print(grid[len(grid)-1][len(grid[0])-1])