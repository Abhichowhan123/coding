# n,k = list(map(int,input().split()))
# print(n,k)
# # print(11%6)
nums = [1,2,3,4,5,6]
k = 11
s = k%(len(nums))
a = (len(nums)-s)
c = len(nums)-1
for i in range(a,len(nums)):
    b= i
    if b<c:
        nums[b],nums[c]=nums[c],nums[b]
    c-=1
d = a-1
for j in range(a):
    bb = j
    if bb<d:
        nums[bb],nums[d]=nums[d],nums[bb]
    d-=1
cc =  len(nums)-1
for k in range(len(nums)):
    aa = k
    if aa<cc:
        nums[aa],nums[cc]=nums[cc],nums[aa]
    cc-=1
for o in nums:
	print(o,end=" ")









# n = int(input())
# A =list(map(int,input().split()))
# k=int(input())
# B=[0]*len(A)
# for i in range(len(A)):
#     if k>4:
#         k= 0
#     B[k]=A[i]
#     k+=1
# print(B)
#

#
# nums= [1,2,3,4,5,6,7]
# k = 3
# B = [0]*len(nums)
# for i in range(len(nums)):
#     B[(i+k)%len(nums)] = nums[i]
# print(B)




