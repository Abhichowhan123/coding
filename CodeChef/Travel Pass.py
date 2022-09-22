for  i  in range (int(input())):
    N,A,B = map(int,input().split())
    S = list(input())
    count = 0
    for j in range(N):
        if S[j]=="0":
            count+=(1*A)
        elif S[j]=="1":
            count+=(1*B)
    print(count)