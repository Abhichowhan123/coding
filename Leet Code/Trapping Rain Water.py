n = int(input())
A = list(map(int,input().split()))

# A = [0,1,0,2,1,0,1,3,2,1,2,1]
prefix = []
suffix = []
max = 0
for i in range(len(A)):
    if max<=A[i]:
        max = A[i]
    prefix.append(max)
print(prefix)
max1 = 0
for j in range(len(A)-1,-1,-1):
    if max1<=A[j]:
        max1 = A[j]
    suffix.insert(0,max1)
print(suffix)
add = 0
for k in range(len(A)-1):
    a = min(prefix[k],suffix[k])
    add = add +(a-A[k])
print(add)


# A = [0,1,0,2,1,0,1,3,2,1,2,1]
# def p(a):
#     pmax = []
#     mo = 0
#     for i in range(a+1):
#         if mo<A[i]:
#             mo = A[i]
#             pmax.append(mo)
#         else:
#             pmax.append(mo)
#     # print(pmax)
#     return max(pmax)
# def s(b):
#     smax = []
#     moo = 0
#     for j in range(len(A)-1,b-1,-1):
#         if moo<A[j]:
#             moo = A[j]
#             smax.append(moo)
#         else:
#              smax.append(moo)
#     smax.reverse()
#     # print(smax)
#     return max(smax)
# add = 0
# for k in range(1,len(A)-1):
#     decide = min(p(k-1),s(k+1))
#     if decide> A[k] :
#         add+=(decide -A[k])
# print(add,"\n")