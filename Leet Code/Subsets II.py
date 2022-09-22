nums = [0]
nums = sorted(nums)
A  =[]
def subsets(temp,i):
    if temp not  in A:
        A.append(temp)
    if i>len(nums)-1:
        return
    for j in range(i,len(nums)):
        subsets(temp+[nums[j]],j+1)
subsets([],0)
print(A)