# A = [1,2,3,4,5,6,7,8,9]
# B = []
# def com(q,w,T,j):
#     if q==0:
#         if w==0:
#             B.append(T)
#             return
#         return
#     for i in range (j,len(A)):
#         com(q-1,w-A[i],T+[A[i]],i+1)
#
# com(q=3,w=9,T = [],j=0)
# print(B)
k = 3
n = 15
result = []
A =  [1,2,3,4,5,6,7,8,9]
def combination(temp,total,i,k,n):
    if total==n and len(temp)==k:
        result.append(temp)
        return
    if i>len(A) or len(temp)>k:
        return
    for j in range(i,len(A)):
        combination(temp+[A[j]],total+A[j],j+1,k,n)
combination([],0,0,k,n)
print(result)