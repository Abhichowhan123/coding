nums = [1,2,3,4]
pre = []
suf = [0]*len(nums)
ans = [0]*len(nums)
a = 1
for i in range(len(nums)):
    a*=nums[i]
    pre.append(a)
a= 1
for j in range(len(nums)-1,-1,-1):
    a*=nums[j]
    suf[j] = a
for i in range(len(nums)):
    if i == 0:
        ans[i] = suf[i+1]
    if i == len(nums)-1:
        ans[i] = pre[len(nums)-2]
    if i !=0 and i!= len(nums)-1:
        ans[i] = pre[i-1]*suf[i+1]
print(ans)