import collections
board = [["8","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]

row = collections.defaultdict(set)
col = collections.defaultdict(set)
matrix  =collections.defaultdict(set)
for i in range(9):
        for j in range(9):
                if board[i][j]==".":
                        continue
                if board[i][j] in row[i] or board[i][j] in col[j] or board[i][j] in matrix[i//3,j//3]:
                        print(False)
                        break
                col[j].add(board[i][j])
                row[i].add(board[i][j])
                matrix[i//3,j//3].add(board[i][j])
print(True)