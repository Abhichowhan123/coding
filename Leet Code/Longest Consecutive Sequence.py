nums =  [0,3,7,2,5,8,4,6,0,1]
B = set(nums)
A = {}
for i in range(len(nums)):
    if nums[i]-1 not in B:
        A[nums[i]] = True
count = 0
for j in A:
    n = j
    c = 0
    b = len(nums)
    while n in B:
        n+=1
        c+=1
        count = max(count,c)
print(count)