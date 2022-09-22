vertix,eges = map(int,input().split())
matrix = [[0]*vertix for i in range (vertix)]

for j in range(eges):
    u,v,w=map(int,input().split())
    u = u-1
    v = v-1
    matrix[u][v] = w

max = 999999
ss = 0
G = matrix
MST = [0, 0, 0, 0, 0, 0]
MST[0] = True
no_edgs = 0
while (no_edgs < vertix - 1):

    a = b = 0
    min = max
    for j in range(vertix):
        if MST[j]:
            for i in range(vertix):
                if G[j][i] != 0 and not MST[i]:
                    if min > G[j][i]:
                        min = G[j][i]
                        a = j
                        b = i
    ss= ss +min
    MST[b] = True
    no_edgs += 1
print(ss)
