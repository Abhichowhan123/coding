nums =[5,4,-1,7,8]
count = nums[0]
c=  0
for i in range(0,len(nums)):
    if c<0:
        c = 0
    c+=nums[i]
    count = max(c,count)
print(count)