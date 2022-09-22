nums = [96,44,99,25,61,84,88,18,19,33,60,86,52,19,32,47,35,50,94,17,29,98,22,21,72,100,40,84]
nums = set(nums)
k = 35
count = 0
i  = 1
num = k*(k+1)//2
for i in nums:
    if i <=k:
        count+=1
        num-=i
while count!=0:
    k+=1
    if k not in nums:
        num+=k
        count-=1
print(num)