# nums = [5,4,0,3,1,6,2]
# count = 0
# for i in range(len(nums)):

#     if nums[i]>=0:
#         ind = nums[i]
#         val = i
#         c = 1
#         while(ind!=i):
#             c+=1
#             temp = nums[ind]
#             nums[ind] = -(val+1)
#             val =ind
#             ind  = temp
#         if count<c:
#             count = c
#         nums[ind] = -(val+1)
# print(count)

nums = [2,2,1,1,1,2,2]
nums.sort()
c = len(nums)//2
print( nums[c])