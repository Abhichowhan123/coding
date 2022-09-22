nums = [2,2]
target = 2
left,right = 0,len(nums)-1
while left<= right:
    mid =(left + right)//2
    if nums[mid]==target:
        le=mid
        while nums[le]==target and le >=0:
            le -= 1
        l =le+1
        ri=mid
        while ri<=len(nums)-1 and ri>=0 and nums[ri]==target:
            ri += 1
        r = ri-1
        print()[l,r]
    elif nums[mid]<target:
        left=mid+1
    else:
        right=mid-1
else:
    print() [-1,-1]











# A =[]
# B  = [-1,-1]
# b = 0
# first = 0
# last = len(nums)-1
# if len(nums)==2:
#     if nums[first]!=target and nums[last]!=target:
#         print(B)
#     if nums[first]==target and nums[last]==target:
#         A.append(0)
#         A.append(1)
#         print(A)
# else:
#     while(first<=last):
#         if nums[0]==target:
#             A.append(0)
#             b += 1
#             break
#         else:
#             mid =(first+last)//2
#             if nums[mid]==target and nums[mid-1]!=target :
#                 A.append(mid)
#                 b+=1
#                 break
#             if target<=nums[mid] and nums[mid-1]!=target or target<=nums[mid]:
#                 last = mid-1
#             else:
#                 first=mid+1
#     first = 0
#     last = len(nums)-1
#     while(first<=last):
#         if nums[len(nums)-1]==target:
#             A.append(0)
#             b += 1
#             break
#         else:
#             mid =(first+last)//2
#             if nums[mid]==target and nums[mid+1]!=target :
#                 A.append(mid)
#                 b+=1
#                 break
#             if target>=nums[mid] and nums[mid+1]!=target or target>=nums[mid]:
#                 first = mid+1
#             else:
#                 last=mid-1
#
#     if b>0:
#         print(A)
#     else:
#         print(B)
