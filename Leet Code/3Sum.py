# nums = [-1,0,1,2,-1,-4]
# A = []
# nums= sorted(nums)
# for i in range(len(nums)):
#     j = i+1
#     k = len(nums)-1
#     while j<k:
#         B = []
#         a = nums[j]+nums[k]
#         if a== (-nums[i]):
#             B.append(nums[i])
#             B.append(nums[j])
#             B.append(nums[k])
#             if B not in A:
#                 A.append(B)
#         if (-nums[i])>a:
#             j+=1
#         else:
#             k-=1
# print(A)

nums = [-1,0,1,2,-1,-4]
A= []
nums = sorted(nums)
for  i in range(len(nums)):
    j = i+1
    k = len(nums)-1
    while j<k:
        B = []
        if nums[j]+nums[k]==(-nums[i]):
            B.append(nums[i])
            B.append(nums[j])
            B.append(nums[k])
            if B not in A:
                A.append(B)
        if nums[j]+nums[k] < -nums[i]:
            j+=1
        else:
            k-=1
print(A)














