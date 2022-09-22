board = [["C","A","A"],
         ["A","A","A"],
         ["B","C","D"]]
word = "AAB"
m,n,W  = len(board),len(board[0]),{1: 0}
is_valide = [[False for x in range(n)] for y in range(m)]
def search(s,i,j,temp,n,m,is_valide):
    if i >= m or j >= n or j <= -1 or i <= -1 or W[1]>0:return
    is_valide[i][j] = True
    if word == temp:W[1]+=1
    else:
        if j != n - 1 and is_valide[i][j + 1] == False and board[i][j + 1] == word[s]:
            search(s + 1, i, j + 1, temp + word[s], n, m, is_valide)
        if i != -1 and is_valide[i - 1][j] == False and board[i - 1][j] == word[s]:
            search(s + 1, i - 1, j, temp + word[s], n, m, is_valide)
        if j != -1 and is_valide[i][j - 1] == False and board[i][j - 1] == word[s]:
            search(s + 1, i, j - 1, temp + word[s], n, m, is_valide)
        if i != m - 1 and is_valide[i + 1][j] == False and board[i + 1][j] == word[s]:
            search(s + 1, i + 1, j, temp + word[s], n, m, is_valide)
        is_valide[i][j] = False
        s -= 1
for i in range(m):
    for j in range(n):
        if board[i][j]==word[0]:
            search(1,i,j,""+word[0],n,m,is_valide)
if W[1]>0:print(True)
else:print(False)
