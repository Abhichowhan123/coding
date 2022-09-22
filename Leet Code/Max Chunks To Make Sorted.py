arr =[1,0,2,3,4]
s1,s2,c = 0,0,0
for i in range(len(arr)):
    s1 += i+1
    s2+=arr[i]+1
    if s1==s2:
        c+=1
print(c)
