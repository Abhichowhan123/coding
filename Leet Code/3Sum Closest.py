# nums = [1,1,-1,-1,3]
# nums = sorted(nums)
# target = -1
# upt = 999999999
# ans= 0
# for i in range(len(nums)-2):
#     j = i+1
#     k = len(nums)-1
#     if nums[i]+nums[j]+nums[k]==target:
#         ans = target
#         break
#     while(j<k):
#         if abs(nums[i]+nums[j]+nums[k]-target)<upt:
#             upt = abs((nums[i]+nums[j]+nums[k])-target)
#             ans  =nums[i]+nums[j]+nums[k]
#         if nums[i]+nums[j]+nums[k]>target:
#             k-=1
#         else:
#             j+=1
# print(ans)

