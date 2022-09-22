A = [1,2,3,4,5]
# pre = [0]*int(len(A)+1)
# max  = 0
# for i in range(len(A)):
#     if A[i]>max:
#         max = A[i]
#     pre[i] =max

# maxx = 0
# pmax = []
# for i in range(y+1):
#     if maxx < p*A[i]:
#         maxx = p*A[i]
#         pmax.append(maxx)
#     else:
#         pmax.append(maxx)
# return max(pmax)
C = [1,2,3]
B = []
for a in C:
    m=-9999999
    for h in A:
        m = max(m,a*h)
    B.append(m)
w = 0
for o in B:
    w+=o
print(w)


