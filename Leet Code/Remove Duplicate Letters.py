s = "cbaacabcaaccaacababa"
count = {}
B= {}
for i in s:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
for j,k in count.items():
    B[j] = False
stack = []
for l in s:
    if B[l] == False and count[l]>0:
        if len(stack)==0:
            stack.append(l)
        else:
            if stack[-1]< l:
                stack.append(l)
            else:
                while stack[-1] > l  and len(stack)!=1:
                    if count[stack[-1]]>0:
                        B[stack.pop()] = False
                    else:
                        break
                if count[stack[-1]] > 0 and stack[-1]> l:
                    B[stack.pop()] = False
                    stack.append(l)
                else:
                    stack.append(l)
        B[l] =True
        count[l]-=1
    else:
        count[l] -= 1
print("".join(stack))

# test
# "bbcaac" "bac"
# "ecbacba" "eacb"




# {'c': 4, 'b': 2, 'e': 1, 'a': 1, 'd': 1}
# {'c': False, 'b': False, 'e': False, 'a': False, 'd': False}