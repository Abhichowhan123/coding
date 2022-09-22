def merge( L, R):
    smaller ,i ,j= 0,0,0
    ans = []
    while i < len(L) and j < len(R):
        if L[i][1] > R[j][1]:
            ans.append(R[j])
            smaller += 1
            j += 1
        else:
            ans.append(L[i])
            res[L[i][0]] += smaller
            i += 1
    while i < len(L):
        ans.append(L[i])
        res[L[i][0]] += smaller
        i += 1
    while j < len(R):
        ans.append(R[j])
        j += 1
    return ans
def mergeSort( nums):
    n = len(nums)
    if n == 1:
        return nums
    mid = n // 2
    L = mergeSort(nums[:mid])
    R = mergeSort(nums[mid:])
    return merge(L, R)
nums = [5,2,6,1]
n = len(nums)
nums = [[i, nums[i]] for i in range(n)]
res = [0]*len(nums)
mergeSort(nums)
print(res)











# nums = [5,2,6,1]
# stack  = []
# result =  [0]*len(nums)
# for i in range(len(nums)-1,-1,-1):
#     if i==len(nums)-1:
#         stack.append(nums[i])
#     elif i !=len(nums)-1:
#         if nums[i+1]<nums[i]:
#             result[i] = len(stack)
#             stack.append(nums[i])
#         else:
#             while stack  and stack[-1]>=nums[i]:
#                 stack.pop()
#             result[i] = len(stack)
#             stack.append(nums[i])
# print(result)

