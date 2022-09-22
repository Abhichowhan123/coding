nums = [1, 5, 9, 1, 5, 9]
k = 2
t = 3
if t==0 and len(nums)==len(set(nums)):print(False)

for i in range(len(nums)):
    for j in range(i+1,min(i+1+k,len(nums))):
        if j>=len(nums):
            break
        if abs(nums[i]-nums[j])<=t:
            print(True)
print(False)




















# nums = [1,5,9,1,5,9]
# t = 3
# k = 2
# if t==0 and len(nums)==len(set(nums)):
#     print("False")
# else:
#     for i in range(len(nums)):
#         for j in range(i+1,min(i+k+1,len(nums))):
#             # if j>= len(nums):
#             #     break
#             if abs(nums[i]-nums[j])<=t:
#                 print("True")
#
#     print("False")





# nums = [1,5,9,1,5,9]
# t = 3
# b =0
# for i in range(len(nums)):
#     k = 2
#     j= i+1
#     n = i
#     while k!=0 and n!=len(nums)-1 :
#         if abs(nums[i]-nums[j])<=t:
#             print("True")
#             b+=2
#             break
#         k-=1
#         j+=1
#         n+=1
#     break
# if b==0:
#     print("False")