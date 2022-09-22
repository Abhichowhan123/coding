target = 11
nums = [1,1,1,1,1,1,1,1]
minn = 99999999
A = []
a = 0
for i in range(len(nums)):
    A.append(nums[i])
    a += nums[i]
    while a>=target:
        minn = min(minn,len(A))
        a-=A.pop(0)
if minn==99999999:
    print(0)
else:
    print(minn)
