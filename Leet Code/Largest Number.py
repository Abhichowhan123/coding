nums =  [0,0]
A = ""
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        a = ""
        b = ""
        a+=str(nums[i])
        b+=str(nums[j])
        if a+b<b+a:
            nums[i],nums[j]=nums[j],nums[i]
    A+=str(nums[i])
if A[0]=="0":
    print(0)
else:
    print(A)
