a = [[1,1],
     [1,1]]

ans = 0
for i in range(len(a)):
    for j in range(len(a)):
        ans+=a[i][j]*(i+1)*(j+1)*(len(a)-i)*(len(a)-j)
        print(ans)
