nums = [0,1,2,2,3,0,4,2]
val = 2
i = 0
n =m  = len(nums)

count  =0
while i!=n:
    if nums[i]==val:
        count+=1
        del nums[i]
        i-=1
        n-=1
    i+=1
print(m-count)


# nums = [45192,0,-659,-52359,-99225,-75991,0,-15155,27382,59818,0,-30645,-17025,81209,887,64648]
# i = 0
# n = len(nums)
# while i!=n:
#     if nums[i]==0:
#         del nums[i]
#         i-=1
#         n-=1
#         nums.append(0)
#     i+=1
# print(nums)