x = 8
l = 0
r = x
ans  =0

while l<=r:
    m = (l+r)//2
    if m*m==x:
        print(m)
    if m*m>x:
        r = m-1
    else:
        l=m+1
        ans = m
print(ans)
