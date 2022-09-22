nums = [-3,-2,-1,0,0,1,2,3]
nums = sorted(nums)
target = 0
A  = []
update = 999999999
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        a = j+1
        b = len(nums)-1
        while a<b:
            B = []
            if nums[i]+nums[j]+nums[a]+nums[b]==target:
                B.append(nums[i])
                B.append(nums[j])
                B.append(nums[a])
                B.append(nums[b])
                if B not in A:
                    A.append(B)

            if nums[i]+nums[j]+nums[a]+nums[b]>target:
                b-=1
            else:
                a+=1
print(A)

# [[-3,-2,2,3],[-3,-1,1,3],[-3,0,0,3],[-3,0,1,2],[-2,-1,0,3],[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]