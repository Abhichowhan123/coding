import math

nums = [3,6,9,1]
A = [0]*len(nums)
interval= math.ceil((max(nums)-min(nums))/len(nums)-1)
