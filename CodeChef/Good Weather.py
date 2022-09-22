for i in range(int(input())):
    A = list(map(int,input().split()))
    sunn = 0
    rain = 0
    for j in range(len(A)):
        if A[j]==1:
            sunn+=1
        else:
            rain+=1
    if sunn>rain:
        print("YES")
    else:
        print("NO")