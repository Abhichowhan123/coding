for i in range(int(input())):
    N = int(input())
    A = list(map(int,input().split()))
    P =0
    Q =0
    count = 0
    k = p =0
    # A = sorted(A)
    for j in A:
        P += j
    for k in range(N):
        Q += A[k]
        P -= A[k]
        q = Q/(k+1)
        if (N-k-1) !=0:
            p = P/(N-k-1)
            if p+q>count:
                count = p+q
            continue
    print(count)
