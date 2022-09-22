# import heapq
# nums = [1,1,1,2,2,3,4]
# k = 2
#
# dic = {}
# A = []
# for i in nums:
#     if i not in dic:
#         dic[i] = 1
#     else:
#         dic[i]+=1
# for a,b in dic.items():
#     if len(A)<k:
#         heapq.heappush(A, (b, a))
#     else:
#         heapq.heappushpop(A, (b, a))
# print([key[1] for key in A])
nums = [1,1,1,2,2,3]
k = 2
A = {}
for i in range(len(nums)):
    if nums[i]in A:
        A[nums[i]]+=1
    else:
        A[nums[i]]=1
A = sorted(A.items(),key= lambda x:x[1],reverse= True)
B = []
for i in range(k):
    B.append(A[i][0])
print(B)