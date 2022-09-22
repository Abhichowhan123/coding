import collections
s = "ABAB"
k = 2
A={}
MAX = -99999999
queue = collections.deque()
count = 0
for i in s:
    if i in A:
        A[i]+=1
    else:
        A[i]=1
    queue.append(i)
    if (len(queue)-max(A.values()))<=k:
        MAX = max(MAX,len(queue))
    else:
        A[queue.popleft()]-=1
print(MAX)