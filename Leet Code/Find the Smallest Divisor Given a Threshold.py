# import math
# nums =  [200,100,14]
# threshold = 10
# def Threshold(threshold, h, l):
#     w = 99999999
#     while l<=h:
#         m = int((h + l )/ 2)
#         a = 0
#         for i in nums:
#             a += math.ceil(i / m)
#         if a <= threshold:
#             if w>m:
#                 w=m
#             h = m - 1
#         if a >= threshold:
#             l = m + 1
#     return w
# h = max(nums)
# l  = 1
# q = Threshold(threshold,h,l)
# print(q)
import math
nums =  [1,2,5,9]
threshold = 6
def Threshold(threshold, h, l):
    w = 99999999
    while l<=h:
        m = (h + l )// 2
        a = 0
        for i in nums:
            a += math.ceil(i / m)
        if a > threshold:
            l = m + 1
        else:
            w = min(w,m)
            h = m - 1
    return w
h = max(nums)
l  = 1
print(Threshold(threshold,h,l))

