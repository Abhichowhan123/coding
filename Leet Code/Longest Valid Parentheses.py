s = ")()())"
stack = [-1]
count = 0
for i in range(len(s)):
    if s[i]=="(":
        stack.append(i)
    else:
        e = stack.pop()
        if len(stack)==0:
            stack.append(i)
        else:
            count  = max(count,(i-stack[-1]))
print(count)


















# A = {")":"("}
# stack = []
# count= 0
# m =0
# for i in s:
#     if i not in A:
#         stack.append(i)
#     else:
#         if len(stack)==0:
#             count  =0
#         else:
#             if stack[-1]==A[i]:
#                 count+=2
#                 m = max(m,count)
#                 stack.pop()
# a = len(stack)*2
#
# print(m-a)