A = [3,-1,5,2,-5]
A = sorted(A)
b = len(A)
a = A[0]*A[1]*A[len(A)-1]
v = A[b-1]*A[b-2]*A[b-3]
print(max(a,v))