
s = "abcd"
k = 4
s = list(s)
for l in range(0,len(s),k*2):
    r = s[l:l+k]
    p = 1
    for j in range(l,l+len(r)):
        s[j]  =r[-p]
        p+=1
print("".join(s))
