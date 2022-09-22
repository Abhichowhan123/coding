s = "cbaebabacd"
p = "abc"
A = []
if len(s)<len(p):
    print(A)

check = "".join(sorted(p))
n = len(p)
i = 0
st = ""
A = []
while len(s)+1!=n:
    a = "".join(sorted(s[i:n]))
    if a == check:
        A.append(i)
    i+=1
    n+=1
print(A)