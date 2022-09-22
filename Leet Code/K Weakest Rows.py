
# n,m =map(int,input().split())
# W = list(map(int,input().split()))
# A = []
# s = 0
# e = m
# for o in range(n):
#     A.append(W[s:e])
#     s+=m
#     e+=m
A=[[1,1,0,0,0],
   [1,1,1,1,0],
   [1,0,0,0,0],
   [1,1,0,0,0],
   [1,1,1,1,1]]
B= {}
for i in range(len(A)):
    l = 0
    h=len(A[0])-1
    j = 0
    while l<=h:
        m= (l+h)//2
        if m==len(A[0])-1 and A[i][m]==1:
            B[i] = 0
            break
        elif m==0 and A[i][m]==0:
            B[i] =len(A)-1
            break
        elif A[i][m]==0 and A[i][m-1]==1 :
            B[i]=(len(A)-1)-m
            break

        elif A[i][m]==0:
            h = m-1
        elif A[i][m]==1:
            l = m+1
print(B)
B =sorted(B.items(), key=lambda x: x[1], reverse=True)
for y,u in B:
    print(y,end=" ")