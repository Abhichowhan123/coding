# def peak(l,h):
#     m = (l+h)//2
#     if len(nums)==1:
#         return 0
#     elif m==0 and nums[m]>nums[m+1]:
#         return(m)
#     elif m==len(nums)-1 and nums[m]>nums[m-1]:
#         return m
#     elif nums[m]>nums[m-1] and nums[m]>nums[m+1]:
#         return m
#     e = peak(m+1,h)
#     if e :
#         return e
#     f = peak(l,m-1)
#     if f:
#         return f
# nums = [3,2,1]
# print(peak(l = 0,h= len(nums)-1))
def peak(l,h):
    l ,h =0, len(nums)-1
    while(l<h):
        m = (l+h)//2
        if nums[m]<nums[m+1]:
            l = m+1
        else:
            h = m
    return l

nums = [1,2,1,3,5,6,4]

print(peak(l = 0,h= len(nums)-1))