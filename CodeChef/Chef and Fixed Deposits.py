for j in range(int(input())):
    n,x = list(map(int,input().split()))
    A =list(map(int,input().split()))
    A.sort(reverse=True)
    a=i = 0
    d = False
    for i in range(len(A)):
        a += A[i]
        if a>=x:
            d=True
            break

    if d==True:
        print(i)
    else:
        print("-1")


# def rec(i,x,sum,count):
#     global a
#     if i ==len(A) or sum>=x:
#         if sum>=x and a>count:
#             a=count
#         return
#     rec(i+1,x,sum+A[i],count+1)
#     rec( i + 1, x, sum,count)
# # x  = 7
# # A = [4,3,5,1]
# for i in range(int(input())):
#     n,x = list(map(int,input().split()))
#     A =list(map(int,input().split()))
#     sum = i = count = 0
#     a = 999999999
#     rec(i,x,sum,count)
#     if a==999999999:
#         print("-1")
#     else:
#         print(a)




# def rec(B,i,x,sum,a):
#     if i == len(A):
#         for h in range(len(B)):
#             sum+=B[h]
#         if sum >= x:
#             T.append(len(B))
#         return
#     rec(B+[A[i]],i+1,x,sum,a)
#     rec(B,i+1,x,sum,a)
#     # return -88
# for i in range(int(input())):
#     n,x = list(map(int,input().split()))
#     A =list(map(int,input().split()))
#     # x  = 7
#     B = []
#     # A = [4,2,5,1]
#     a=99999999
#     T = []
#     sum = i = 0
#     rec(B,i,x,sum,a)
#     if len(T)<=0:
#         print(-1)
#     else:
#         print(min(T))