import numpy
r,t = map(int,input().split())
A = list(map(int,input().split()))
B = []
for h in range(t):
    f = list(map(int,input().split()))
    B.append(f)
q = w = 0
max = 0
C = []
for i in B:
    k=0
    for j in range(B[w][q]-1,B[w][q+1]):
        k =k+A[j]
    C.append(k)
    w+=1
for l in range(len(C)):
    p = 0
    for m in range(l,len(C)):
         p = p+C[m]
    if p>max:
        max = p
print(max)
#
# A = [1,-2,1,3,-4]
# B = [[0,1],[3,4],[2,3],[0,3]]
# q = w = k = 0
# max = 0
# C = []
#
# for i in B:
#     for j in range(B[w][q],B[w][q+1]+1):
#         k =k+A[j]
#     C.append(k)
#     w+=1
# for l in range(len(C)):
#     p = 0
#     for m in range(l,len(C)):
#          p = p+C[m]
#     if p>max:
#         max = p
# print(max)