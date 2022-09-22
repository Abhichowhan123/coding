import  math
n = 20
pr = [1]*n
pr[1] = 0
f = int(math.sqrt(n))
for i in range(2,f+1):
    if pr[i]==1:
        for j in range(i,f+1):
            pr [i*j] = 0
print(pr)