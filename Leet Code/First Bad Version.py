
l = 0
h = n
while(l<h):
    m = (l+h)//2
    if isBadVersion(m):
        h = m
    else:
        l = m+1
