nums = [2, 1, 2]
nums = sorted(nums,reverse=True)
p = 0
for i in range(len(nums)-2):
    if nums[i+1]+nums[i+2]>nums[i]:
        p = nums[i+1]+nums[i+2]+nums[i]
        print(p)
        break
