nums1 = [2,4]
nums2 = [1,2,3,4]
stack = []
A = {}
for i in range(len(nums2)-1,-1,-1):
    while stack and stack[-1]<nums2[i]:
        stack.pop()
    if len(stack)==0 or stack[-1]<nums2[i]:
        A[nums2[i]] = -1
        stack.append(nums2[i])
    else:
        if nums2[i]<stack[-1]:
            A[nums2[i]] = stack[-1]
            stack.append(nums2[i])
stack = []
for j in nums1:
    stack.append(A[j])
print(stack)