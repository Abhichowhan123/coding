nums1 = [-1,1,1,1,-1]
nums2 = [0,-1,-1,0,1]
nums3 = [-1,-1,1,-1,-1]
nums4 = [0,1,0,-1,-1]
A = {}
count = 0
prefsum = 0
for i in nums3:
    for j in nums4:
        a = i+j
        if a in A:
            A[a]+=1
        else:A[a] = 1

for i in nums1:
    for j in nums2:
        a= -(i+j)
        if a in A:
            count+=A[a]
print(count)