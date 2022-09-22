import collections
import heapq
from collections import Counter

tasks = ["A","A","A","B","B","B"]
n = 2
count = Counter(tasks)
mheap  =[-i for i in count.values()]
heapq.heapify(mheap)

time = 0
q = collections.deque()
while mheap or q:
    time+=1
    if mheap:
        cnt = 1+heapq.heappop(mheap)
        if cnt:
            q.append([cnt,time+n])
    if q and q[0][1]==time:
        heapq.heappush(mheap,q.popleft()[0])
print(time)