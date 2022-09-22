n = 5
"""Output: [[".Q..","...Q","Q...","..Q."],
         ["..Q.","Q...","...Q",".Q.."]]"""
colpos = set()
leftdigo = set()
rigthdio=go = set()
bord = [["."]*n for i in range(n)]
result=  []
def queens(r):
    if r ==n:
        A  =["".join(r)for r in bord]
        result.append(A)
        return
    for c in range(n):
        if c in colpos or (r-c)in leftdigo or (r+c) in rigthdio:
            continue
        colpos.add(c)
        leftdigo.add(r-c)
        rigthdio.add(r+c)
        bord[r][c] = "Q"

        queens(r+1)

        colpos.remove(c)
        leftdigo.remove(r - c)
        rigthdio.remove(r + c)
        bord[r][c] = "."
queens(0)
print(result)