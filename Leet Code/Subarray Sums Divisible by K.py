nums = [4, 5, 0, -2, -3, 1]
k = 5
A= {0:1}
count = 0
presum = 0
for i in nums:
    presum+=i
    if presum%k in A:
        count+=A[presum % k]
    if presum%k in A:
        A[presum % k] += 1
    else:
        A[presum%k] = 1
print(count)