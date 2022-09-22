
import collections
nums = [1,3,-1,-3,-2,5,3,6,7]
k = 3
A = []
l = 0
queue = collections.deque()
for i in range(len(nums)):
    while queue and nums[queue[-1]]<nums[i]:
        queue.pop()
    queue.append(i)
    if l>queue[0]:
        queue.popleft()
    if (i+1)>=k:
        l+=1
        A.append(nums[queue[0]])
print(A)


