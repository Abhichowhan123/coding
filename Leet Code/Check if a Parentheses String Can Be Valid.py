s = "((()(()()))()((()()))))()((()(()"
locked = "10111100100101001110100010001001"
stack =[]
for i in range (len(s)):
    if stack and stack[-1][1]=="0" and locked[i]=="0":
        stack.pop()
    elif s[i]==")" and stack:
        if (stack[-1]=="(") or (locked[i]=='1') or (locked[i]=="0" and stack[-1][1]=="0") :
            stack.pop()
        else:
            if locked[i]=="0":
                stack.append([s[i],locked[i]])
    else:
        stack.append([s[i],locked[i]])
if len(stack)==0:
    print(True)
else:
    print(False)













# for i in range(len(s)):
#     if  s[i]=="(" and locked[i]=="0":
#         stack.append(["(",i])
#     elif s[i]==")" and (locked[i]=="0" or locked[i]=='1'):
#         if stack and locked[i]=="1":
#             stack.pop()
#         elif locked[i]=="0":
#             stack.append([s[i], i])
#         else:
#             print(False)
#
# if len(stack)%2==0:
#     print(True)
# else:
#     print(False)