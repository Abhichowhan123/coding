num = [1,3,2]
x = len(num)-1
while x>=0 and num[x]<= num[x-1]:
    x-=1
if x >0:
    w = x
    for k in range(x+1,len(num)):
        if num[x-1]<num[k]:
            w = k
    num[x-1],num[w]=num[w],num[x-1]
    i = x
    j = len(num)-1
    while(i<j):
        num[i],num[j] = num[j],num[i]
        j-=1
        i+=1
else:
    i = 0
    j = len(num) - 1
    while (i < j):
        num[i], num[j] = num[j], num[i]
        j -= 1
        i += 1
print(num)
