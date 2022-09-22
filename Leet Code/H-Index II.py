citations = [0,1,2,3,4,5]
if not citations[-1]:
    print(0)
l = 0
r = len(citations)-1
while l<r:
    m = (l+r)//2
    if citations[m]>=len(citations)-m:
        r = m
    else:
        l = m+1
print(len(citations)-l)