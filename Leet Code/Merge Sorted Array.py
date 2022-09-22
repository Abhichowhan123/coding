nums1 = [0]
nums2 = [1]
m = 0
n = 1
# m = m-1
# n = n-1
a = len(nums1)-1
while(n>0 and m>0):
    if nums1[m-1]>nums2[n-1]:
        nums1[a] = nums1[m-1]
        m-=1
    else:
        nums1[a] = nums2[n-1]
        n-=1
    a-=1
while n>0:
    nums1[a] = nums2[n-1]
    n -= 1
    a -= 1
print(nums1)