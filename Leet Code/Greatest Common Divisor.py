def GCD(a,b):
    mini = min(a,b)
    maxm = max(a,b)
    while (mini!= 0):
        if maxm%mini==0:
            return mini
        temp = maxm
        mini = maxm%mini
        maxm = temp

A = list(map(int,input().split()))
gcd = GCD(A[0],A[1])
for j in range(2,len(A)):
    gcd = GCD(gcd,A[j])
    print(gcd)