nums = [23,2,4,6,7]
k = 6
A={0:-1}
prefsum = 0
for i,n in enumerate(nums):
    prefsum+=n
    a = prefsum%k
    if a not in A:
        A[a]=i
    elif i-A[a]>1:
        print("True")
