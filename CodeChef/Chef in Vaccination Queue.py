for i in range(int(input())):
    N, P, X, Y = map(int,input().split())
    A = list(map(int,input().split()))
    ad = 0
    for j in range(P):
        if A[j]==0:
            ad+=X
        else:
            ad+=Y
    print(ad)