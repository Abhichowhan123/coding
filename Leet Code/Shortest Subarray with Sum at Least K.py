from collections import deque
nums = [2,7,3,-8,4,10]
k = 12
Min=999999999
queue= deque([[0,-1]])
sum=0
for i in range(len(nums)):
    sum += nums[i]
    while queue and (sum-queue[-1][0]>=k):
        Min = min(Min, (queue[0][1]) - queue[-1][1] + 1)
        queue.pop()
    while queue and sum<queue[0][0]:
        queue.popleft()
    queue.appendleft([sum,i])
print(queue[0])

# dq = [(-1, 0)]
# sums, res = 0, float("inf")
# for i, val in enumerate(nums):
#     sums += val
#     while dq and sums-dq[0][1] >= k:
#         res = min(res, i-dq[0][0])
#         dq.pop(0)
#     while dq and sums < dq[-1][1]:
#         dq.pop()
#     dq.append((i, sums))
# print(res)
