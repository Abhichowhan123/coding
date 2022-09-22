nums = [1,2,1]
stack = []
# [4, 3, 2, 1]
A= [0]*len(nums)
for i in range(len(nums)-1,-1,-1):
    if len(stack)==0:
        stack.append(nums[i])
    else:
        while stack and stack[-1]<nums[i]:
            stack.pop()
        stack.append(nums[i])

for j in range(len(nums)-1,-1,-1):
    while stack and stack[-1]<=nums[j]:
        stack.pop()
    if len(stack)==0:
        A[j]=-1
        stack.append(nums[j])
    else:
        A[j] = stack[-1]
        stack.append(nums[j])
print(A)