import math
seats = [0,1]
p,s,a = -1,-1,0
for i in range(len(seats)):
    if seats[i]==1:
        break
    if seats[i]==0:
        p+=1
for i in range(len(seats)-1,-1,-1):
    if seats[i]==1:
        break
    if seats[i]==0:
        s+=1
for j in range(len(seats)):
    if seats[j]==1:
        a = 0
    if seats[j]==0:
        a+=1
    seats[j]=a
if p>=0:
    p+=1
if s>=0:
    s+=1
w  = max(p,s,(math.ceil(max(seats)/2)))
print(w)