s = "Test1ng-Leet=code-Q!"
s = list(s)
r = len(s)-1
l = 0
A ={"[":0,']':0,"^":0,"_":0,"`":0,"{":0,"|":0,"}":0,"~":0}
for i in range(32,65):
    A[chr(i)]  =0
while l<=r:
    if s[l] in A :
        l+=1
    elif s[r] in A:
        r-=1
    else:
        s[l],s[r]=s[r],s[l]
        l += 1
        r -= 1

print("".join(s))
