nums = [1,2,3]
target = 4
dp = [0]*(target+1)
dp[0] = 1
for i in range(1,target+1):
    for n in nums:
        if n<=i:
            dp[i]+=dp[i-n]
print(dp[target])


"""TLE"""
# nums = [1,2,3]
# target = 4
# A = {1:0}
# B = []
# def combination(temp,target,j):
#     if target==0:
#         B.append(temp)
#         A[1]+=1
#         return
#     if j>len(nums) or target<0:return
#     for j in range(0,len(nums)):
#         target-=nums[j]
#         combination(temp+[nums[j]],target,j)
#         target += nums[j]
# combination([],target,0)
# print(B)
# print(A[1])