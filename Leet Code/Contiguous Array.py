nums = [1,1,1,0,0,1,1]
A = {}
prefsum = 0
count = 0
for i in range(len(nums)):
    if nums[i]==0:
        prefsum-=1
    else:
        prefsum+=nums[i]
    if prefsum ==0:
        if count<i+1:
            count = i+1
    if prefsum  in A:
        if count <i-A[prefsum]:
            count = i-A[prefsum]
    else:
        A[prefsum] =i
print(count)