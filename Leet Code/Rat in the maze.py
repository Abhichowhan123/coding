# for o in (input()):
#     n = int(input())
#     l = list(map(int,input().strip()))
#     M = []
#     for i in range(0,len(l),4):
#         e = n
#         j = i
#         m = []
#         while(e>=1):
#             m.append(l[j])
#             j+=1
#             e-=1
#         M.append(m)
M=[[1,0,0,0],
   [1,1,0,1],
   [1,1,0,0],
   [0,1,1,1]]
n=4
E =  []
def printpath(i,j,s):
    if M[i][j]==0  :
        return
    if i==j and  j== n-1:
        E.append(s)
        return
    if i == n-1:
        printpath(i,j+1,s+"R")
    elif j==n-1:
        printpath(i+1,j,s+"D")
    else:
        printpath(i,j+1,s+"R")
        printpath(i+1,j,s+"D")
printpath(i=0,j=0,s = "")
print(" ".join(E))
# for u in E:
#     print(u,end=" ")

