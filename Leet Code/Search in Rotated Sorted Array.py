nums = [4,5,6,7,8,0,1]
target = 1
p = -1
first = 0
end = len(nums)-1
while first<=end:
    m = (first+end)//2
    if target== nums[m]:
        p= m
        break

    if nums[m]>=nums[end]:
        if nums[m]>=target and target>=nums[first]:
            end = m-1
        else:
            first =m+1
    else:
        if nums[end] >= target and target >= nums[m]:
            first = m + 1
        else:
            end = m - 1
if p != -1:
    print(p)
else:
    print(p)