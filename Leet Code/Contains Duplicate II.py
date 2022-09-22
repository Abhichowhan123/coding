nums = [1,0,1,1]
k = 1
A = {}
for i in range(len(nums)):
    if nums[i] not in A:
        A[nums[i]]  =i
    else:
        if abs(A[nums[i]] -i)<=k:
            print(True)
        else:
            A[nums[i]]= i