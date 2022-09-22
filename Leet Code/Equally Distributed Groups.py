for k in range(int(input())):
    n = int(input())
    A = list(map(int,input().split()))
    B = {}
    C= []
    for i in range(n):
        if A[i] in B:
            B[A[i]]+=1
            C.append(B[A[i]])
        elif A[i] not in B:
            B[A[i]] = 1
    count = 0
    for j in range(len(C)):
        if C[1]==C[j]:
            count+=1
    if count == len(B):
        print("true")
    else:
        print("false")














# for i in range(int(input())):
#     N = int(input())
#     A = list(map(int,input().split()))
#     B = []
#     if N%2!=0:
#         print("false")
#     for j in range(N):
#         count = 0
#         for k in range(N):
#             if A[j]==A[k]:
#                 count+=1
#         B.append(count)
#     h = 0
#     for l in range(len(B)):
#         if B[0] == B[l]:
#             h+=1
#     if h==len(B):
#         print("true")
#     else:
#         print("false")
