nums = [1,2,3]
A = []
def subsets(i,B):
    A.append(B)
    if i> len(nums)-1 :
        return
    for j in range(i,len(nums)):
        subsets(j+1,B+[nums[j]])

subsets(0,[])
print(A)




# nums = [1,1,2]
# A=[ ]
# def  Permutations(nums,i):
#     if i==len(nums)-1 and nums not in A:
#         A.append(nums)
#         return
#     for j in range(i,len(nums)):
#         nums[i],nums[j] = nums[j],nums[i]
#         Permutations(nums[:], i+1)
#         nums[i], nums[j] = nums[j], nums[i]
# Permutations(nums,0)
# print(A)



# candidates = [10, 1, 2, 7, 6, 1, 5]
# target = 8
# candidates  =sorted(candidates)
# A = []
# def combination(i,t,B):
#     if t<0:
#         return
#     if t==0 and B not in A:
#         A.append(B)
#         return
#     for j in range(i,len(candidates)):
#         if j>i and candidates[j]==candidates[j-1]:
#             continue
#         combination(j+1,t-candidates[j],B+[candidates[j]])
#
# combination(0,target,[])
# print(A)


# candidates = [3,5,8]
# target = 11
# def combination(i,t,B):
#     if t<0:
#         return
#     if t==0 and B not in A:
#         A.append(B)
#         return
#     for n in range(i,len(candidates)):
#         combination(n,t-candidates[n],B+[candidates[n]])
#         combination(n+1, t-candidates[n], B + [candidates[n]])
# A  = [ ]
# t = target
# combination(0,t,[])
# print(A)