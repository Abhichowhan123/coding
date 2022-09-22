import math
target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]
B ={}
for i in range(len(speed)):
    t = ((target-position[i])/speed[i])
    B[position[i]]=t
B = sorted(B.items(),key= lambda x:x[0],reverse=True)
count = 0
cou = 0
for j in B:
    if j[1]>cou:
        cou =j[1]
        count+=1
print(count)