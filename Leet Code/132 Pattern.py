nums =[1,0,1,-4,-3]
maxn = -999999999999
stack  =[]
for i in range(len(nums)-1,-1,-1):
    while stack and stack[-1]<nums[i]:
        maxn = stack.pop()
    if nums[i]< maxn and len(stack)>0:
        print(True)
    else:
        stack.append(nums[i])
print(False)