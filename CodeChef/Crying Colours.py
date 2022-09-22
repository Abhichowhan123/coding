for j in range(int(input())):
    n = int(input())
    R = list(map(int,input().split()))
    G = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # n = 3
    # R = [2,1,2]
    # G = [1,4,0]
    # B = [2,0,3]
    count = 0
    r=g=b=0
    r1=g1=b1=0
    u = R[1]+R[2]+G[2]
    l = G[0]+B[1]+B[0]
    print(max(l,u))

    # if R[0]==n and G[1]==n and B[2]==n:
    #     print("0")
    # else:
    #     if R[0]!=n:
    #         count+=1
    #         R[1],G[0]=G[0],R[1]
    #     if G[1]!=n:
    #         count+=1
    #         R[2], B[0] = B[0], R[2]
    #     if B[2]!=n:
    #         count += 1
    #         B[1], G[0] = G[0], B[1]
    #     print(count)