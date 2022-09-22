A = [1,2,3]
add = 0
for i in range(len(A)):
    add+= A[i]*(i+1)*(len(A)-i)
print(add)