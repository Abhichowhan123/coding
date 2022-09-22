nums = [0,1]
nums  = sorted(nums)
m = nums[len(nums)-1]
nums  =set(nums)
a = 999999
for i in range(0,len(nums)):
    if i not in nums:
        print(i)
    a = i
if a!= 999999:
    print(m+1)