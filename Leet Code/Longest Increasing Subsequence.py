nums = [10,9,2,5,3,7,101,18]
maxx = -9999
a= 1
for  i in range(1,len(nums)):
    if nums[i-1]<nums[i]:
        a+=1
    else:
        a=1
    maxx = max(a,maxx)