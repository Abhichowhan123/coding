t = int(input())
for k in range(t):
    b = []
    i = 1
    A = list(map(int,input().split()))
    if ((A[i + 1] % A[1])!=0) :
        for i in range(1, len(A)):
            f = int(A[i])
            b.append(f)
        print(*b)
    else:
        for i in range(1, len(A)):
            g = int(A[i] / A[1])
            b.append(g)
        print(*b)





















