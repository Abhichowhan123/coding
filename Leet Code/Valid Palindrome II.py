s = "aba"
i = 0
j = len(s)-1
while i<=j:
    if s[i]==s[j]:
        i+=1
        j-=1
    else:
        d = s[i+1:j+1]
        e = s[i:j]
        if d==d[::-1]:
            print(True)

        elif e==e[::-1]:
            print(True)
        else:
            print(False)
        break
print(True)