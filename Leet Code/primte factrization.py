import math
for i in range(int(input())):
    n = int(input("range of prime no"))
    m = int(input("enter the factization"))
    fact= 1
    A = []
    for j in range(2,n+1):
        f =int( math.sqrt(j))
        count = 0
        for k in range(2,f+1):
            if j%k==0:
                count+=1
        if count == 0:
            print(j, end=" ")
            A.append(j)
    u = 0
    while (m != 1):
        while m % A[u] == 0:
            m = int(m / A[u])
            print("\n",A[u],end=" ")
        u += 1

