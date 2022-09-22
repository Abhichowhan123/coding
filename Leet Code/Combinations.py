
n = 4
k = 2
res = []
def helper(level, comb):
    if len(comb) == k:
        res.append(comb[:])
    else:
        for i in range(level, n + 1):
            comb.append(i)
            helper(i + 1, comb)
            comb.pop()
helper(1, [])
print( res)
