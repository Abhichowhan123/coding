# import math
# A = [-1]*(100001)
# A[0] = A[1]  = -1
# f= int(math.sqrt(100001))
# for j in range(2,f+1):
#     if A[j] == -1:
#         for k in range(j * j, 100001):
#             if k % j == 0:
#                 A[k] = j
#  for h in range(int(input())):
#     n = int(input())
#     B = {}
#     while n!=0:
#         if A[n] == -1:
#             if n in B:
#                 B[n] += 1
#             elif n not in B:
#                 B[n] = 1
#             break
#         if A[n] in B:
#             B[A[n]]+=1
#         elif A[n] not in B:
#             B[A[n]] = 1
#         n = int(n/A[n])
#     sorted(B)
#     for o ,p in B.items():
#         print(o,p)
#
