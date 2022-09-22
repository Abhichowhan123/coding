board =[["t","a","b","n"],
        ["o","t","a","e"],
        ["a","h","k","r"],
        ["a","f","l","v"]]
words = ["oa","oaa"]
m, n, W = len(board), len(board[0]), []
is_valide = [[False for x in range(n)] for y in range(m)]
def search(s, i, j, temp, n, m, is_valide,k):
    if i >= m or j >= n or j <= -1 or i <= -1 : return
    if k == temp :
        if temp not in W:
            W.append(temp)
        return
    else:
        is_valide[i][j] = True
        if j != n - 1 and is_valide[i][j + 1] == False and board[i][j + 1] == k[s]:
            search(s + 1, i, j + 1, temp + k[s], n, m, is_valide,k)
        if i != -1 and is_valide[i - 1][j] == False and board[i - 1][j] == k[s]:
            search(s + 1, i - 1, j, temp + k[s], n, m, is_valide,k)
        if j != -1 and is_valide[i][j - 1] == False and board[i][j - 1] == k[s]:
            search(s + 1, i, j - 1, temp + k[s], n, m, is_valide,k)
        if i != m - 1 and is_valide[i + 1][j] == False and board[i + 1][j] == k[s]:
            search(s + 1, i + 1, j, temp + k[s], n, m, is_valide,k)
        is_valide[i][j] = False
        s -= 1
    return
for k in words:
    for i in range(m):
        for j in range(n):
            if board[i][j] == k[0]:
                search(1, i, j, "" + k[0], n, m, is_valide,k)
print(W)


