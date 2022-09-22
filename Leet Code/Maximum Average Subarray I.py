nums = [0,1,1,3,3]
k = 4
Max = -999999
sum = 0
for i in range(k):
    sum+=nums[i]
Max = max(Max,sum)
d = k
a = 0
while d<len(nums):
    sum = (sum-nums[a])+nums[d]
    Max = max(Max, sum)
    d+=1
    a+=1
print(Max/k)
