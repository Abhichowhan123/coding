nums = [1]
target = 0
l = 0
r = len(nums)
p = 0
if len(nums)==1:
    if target==nums[0]:
        print(True)
    else:
        print(False)
def re1(l,r):
    while(l<r):
        m = (r+l)//2
        if target==nums[m]:
            return (True)
        if target >nums[m]:
            l=m+1
        else:
            r =m-1
    return (False)
while(l<r):
    m = (l+r)//2
    if nums[m]==target:
        print(True)
        break
    if nums[m-1]>nums[m] or nums[m-1]<nums[m]:
        p  =m
        if target>nums[len(nums)-1]:
            print(re1(0,p))
            break
        else:
           print( re1(p,len(nums)-1))
           break

