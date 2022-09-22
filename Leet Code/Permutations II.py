
A = [2, 2, 1, 1]
B = []
def permu(A,i):
    if i ==len(A)-1:
        B.append(A)
        return
    dic = {n: 0 for n in A}
    for j in range(i,len(A)):
        if dic[A[j]] == 0:
            A[i],A[j] = A[j],A[i]
            permu(A[:],i+1)
        dic[A[j]]+=1
permu(A,i=0)
new_k = []
for elem in B:
    if elem not in new_k:
        new_k.append(elem)
k = new_k
print (k)


# A = [2,2,1,1]
# B = []
# def permu(A,i):
#     if i ==len(A)-1:
#         B.append(A)
#         return
#     for j in range(i,len(A)):
#         A[i],A[j] = A[j],A[i]
#         permu(A[:],i+1)
# permu(A,i=0)
# new_k = []
# for elem in B:
#     if elem not in new_k:
#         new_k.append(elem)
# k = new_k
# print (k)