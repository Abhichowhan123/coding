s = "babad"
max = -99999999
w = ""
for i in range(len(s)):
    a,b = i,i
    while a>=0 and b<len(s) and s[a]==s[b]:
        if (b-a+1)>max:
            w = s[a:b+1]
            max = b-a+1
        a-=1
        b+=1
    a ,b = i,i+1
    while a >= 0 and b < len(s)  and s[a] == s[b]:
        if (b - a + 1) > max:
            w = s[a:b + 1]
            max = b - a + 1
        a -= 1
        b += 1
print(w)