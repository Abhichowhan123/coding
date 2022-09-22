tiles = "AAABBC"
tiles = list(tiles)
A = {}
def Letter_Tile(s):
    for i in range(len(tiles)):
        s += tiles[i]
        if s is not A:
            A[s] = 0
    return
def rec(tiles, i):
    Letter_Tile("")
    for j in range(i, len(tiles)):
        tiles[i], tiles[j] = tiles[j], tiles[i]
        rec(tiles, i + 1)
        tiles[i], tiles[j] = tiles[j], tiles[i]
rec(tiles, 0)
print(len(A))


