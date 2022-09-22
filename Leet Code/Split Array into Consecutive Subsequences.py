nums = [1,2,3,3,4,4,5,5]
A = {}
for i in  range(len(nums)):
    if nums[i] not in A:
        A[nums[i]] = 1
    else:
        A[nums[i]]+=1
