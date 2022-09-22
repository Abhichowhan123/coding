nums = [279,169,463,252,94,455,423,315,288,64,494,337,409,283,283,477,248,8,89,166,188,186,128]
dic = {}
for i in range(len(nums)):
    temp =  0
    n = nums[i]
    while n!=0:
        g  = n%10
        temp+=g
        n = n//10
    dic[i] = temp
dj = sorted(dic.items(),key=lambda x:x[1])
A =-999999999
i= 0
for i in range(len(d)-1):
    if d[i][1] == d[i+1][1]:
        a = i
        while 1:
            if a>=len(d)-1 or d[i][1] != d[a+1][1] :
                break
            else:
                A = max(A, (nums[d[i][0]] + nums[d[a + 1][0]]))
                a += 1
if A==-999999999:
    print(-1)
else:
    print(A)
