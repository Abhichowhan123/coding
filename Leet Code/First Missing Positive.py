nums = [1,2,0]

n = len(nums)
if n == 1:
    print ((nums[0] == 1) + 1)
for i in range(n):
    nums[i] = nums[i] * n if nums[i] > 0 else 0
for i in range(n):
    idx = (nums[i] // n) - 1
    if 0 < nums[i] and idx < n and not nums[idx] % n:
        nums[(nums[i] // n) - 1] += 1
for i in range(n):
    if not nums[i] % n:
        print( i + 1)
print( n + 1)

# a = 1
# count  = 0
# if a not in nums:
#     print(a)
# else:
#     for i in range(len(nums)):
#         if a in nums:
#             a+=1
#         else:
#             print(a)
#             break
