for i in range(int(input())):
    n = int(input())
    A = list(map(int,input().split()))
    ecount = ocount = 0
    for j in range(n):
        if A[j]%2==0:
            ecount+=1
        else:
            ocount+=1
    if ecount==n:

        ma = 999999999999999999999999
        for i in range(n):
            count = 0
            while A[i]%2!=1:
                A[i] = (A[i]/2)
                count+=1
            if ma>count:
                ma = count
        print(ma)
    else:
        print("0")
