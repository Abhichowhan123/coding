import heapq
nums1 = [1,7,11]
nums2 = [2,4,6]
k = 3
A = []
B = []
for i in nums1:
    if len(B)==k*2:
        break
    for j in nums2:
        B.append([i,j])
for b in B :
    heapq.heappush(A, (-sum(b),b))
    if len(A)>k:
        heapq.heappop(A)
print([heapq.heappop(A)[1] for j in range(len(A))])
