s ="(])"
dic = {")":"(","}":"{","]":"["}
stack = []
if len(stack)==0 or len(stack)==1:
    print(False)
for i in range(len(s)):
    if s[i] not in dic:
        stack.append(s[i])
    else:
        if  len(stack)>0 :
            if dic[s[i]] == stack[-1] :
                stack.pop()
            else:
                print(False)
        else:
            print(False)


if len(stack)==0:
    print(True)
else:
    print(False)
