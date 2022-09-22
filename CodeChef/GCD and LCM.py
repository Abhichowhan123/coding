a,b = map(int,input().split())
A = []
i = 2
while (a!=0):
    c = a / i
    A.append(i)
    i+=1
print(A)
"""t = int(input())
for i in range(t):
    a,b = map(int,input().split())
    GCD(a,b)
    LCM(a,b)"""