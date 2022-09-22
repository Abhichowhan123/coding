nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
A = []
nums2 =set(nums2)
for i in range(len(nums1)):
    if nums1[i] in nums2:
        if nums1[i] not in A:
            A.append(nums1[i])
print(A)