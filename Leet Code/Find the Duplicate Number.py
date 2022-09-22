nums = [1,3,4,2,2]
A= {}
for  i in range(len(nums)):
    if nums[i]in A:
        print(nums[i])
    else:
        A[nums[i]] = 1