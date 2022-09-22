from collections import Counter

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
nums1 = Counter(nums1)
nums2 = Counter(nums2)
ans = []
for n, c in nums1.items():
    for i in range(min(c, nums2[n])):
        ans.append(n)
print(ans)