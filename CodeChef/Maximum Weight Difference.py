for i in range(int(input())):
    N,K = list(map(int,input().split()))
    W = list(map(int,input().split()))
    W = sorted(W)
    a,b = 0,0
    if K>N//2:
        for i in range(N-K,N):
            a += W[i]
        for j in range(N-K):
            b += W[j]
        print(a-b)
        continue
    else:
        for i in range(K):
            a+=W[i]
        for j in range(K,len(W)):
            b+=W[j]
        print(b-a)
        continue