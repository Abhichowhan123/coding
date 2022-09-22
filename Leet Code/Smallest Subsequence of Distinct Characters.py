s = "bcbcbcababa"
stack = []
check = {}
count = {}
for k in s:
    if k not in check:
        check[k]= 0
for j in s:
    if j not in count:
        count[j]=1
    else:
        count[j]+=1
for i in range(len(s)):
    if check[s[i]]==0 and count[s[i]]>0:
        while stack and stack[-1]>s[i] and count[stack[-1]]>0:
            check[stack.pop()] = 0
        stack.append(s[i])
        count[s[i]] -= 1
        check[s[i]] = 1
    else:
        count[s[i]]-=1
print("".join(stack))