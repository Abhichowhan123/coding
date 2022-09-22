students = [1,1,1,0,0,1]
sandwiches = [1,0,0,0,1,1]
A = {}
for i in range(len(sandwiches)):
    if students[i] in A:
        A[students[i]]+=1
    else:
        A[students[i]] = 1
for i in range(len(sandwiches)):
    if A[sandwiches[i]]!=0:
        A[sandwiches[i]]-=1

print(A)