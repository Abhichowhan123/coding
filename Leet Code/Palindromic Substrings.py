s = "aaa"
count = 0
for i in range(len(s)):
    a = i
    b = i
    while b<len(s):
        q = s[a:b+1]
        if q ==q[::-1]:
            count+=1
        b+=1