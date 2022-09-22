for i in range(int(input())):
    N,M,K = map(int,input().split())
    if N>M*K:
        print("YES")
    else:
        print("NO")