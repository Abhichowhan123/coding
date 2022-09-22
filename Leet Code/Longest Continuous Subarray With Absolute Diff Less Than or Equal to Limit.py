from collections import deque
nums =[8,2,4,7]
limit = 4

minq =deque()
maxq = deque()
maxlen =start = 0
for end in range(len(nums)):
    num = nums[end]
    while len(maxq) != 0 and maxq[-1][0] <= num:
        maxq.pop()
    maxq.append((num, end))
    while len(minq) != 0 and minq[-1][0] >= num:
        minq.pop()
    minq.append((num, end))
    while start < end and (maxq[0][0] - minq[0][0]) > limit:
        if maxq[0] == (nums[start], start):
            maxq.popleft()
        if minq[0] == (nums[start], start):
            minq.popleft()
        start += 1
    maxlen = max(maxlen, end - start + 1)
print(maxlen)




