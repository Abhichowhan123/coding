A = [1,2,3]
B = []
def permutation(A,i):
    if i == len(A)-1:
        B.append(A)
        return
    for j in range(i,len(A)):
        A[i], A[j] = A[j], A[i]
        permutation(A[:],i+1)
        A[i], A[j] = A[j], A[i]

permutation(A,i = 0)
print(B)