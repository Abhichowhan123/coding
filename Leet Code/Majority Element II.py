import math
nums = [3,2,3]
A = []
b = (len(nums)/3)
B = {}
for i in nums:
    if i in B:
        B[i]+=1
    else:
        B[i]  =1
for j,a in B.items():
    if a>b:
        A.append(j)
print(A)
