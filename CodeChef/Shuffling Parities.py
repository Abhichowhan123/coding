for j in range (int(input())):
    N = int(input())
    ev = od = 0

    A = list(map(int,input().split()))
    for i in range(N):

        if A[i]%2==0:
            ev+=1
        elif A[i]%2==1:
            od+=1
    if ev<(N+1)/2:
        a = ev
    else:
        a = int((N+1)/2)
    if od<N/2:
        b= od
    else:
        b = int(N/2)
    a=a+b
    print(a)