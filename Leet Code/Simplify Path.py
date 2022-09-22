path = "/../"
path+="/"
stack = []
a= ""
for i in range(len(path)):
    if path[i]=="/":
        if a =="..":
            if stack:
                stack.pop()
        elif len(a)>0 and a!=".":
            stack.append(a)
        a = ""
    else:
        a+=path[i]
print("/"+"/".join(stack))






















# for i in range(len(path)):
#
#     if path[i] == "/" :
#         if len(s)>0:
#             stack.append(s)
#         s = ""
#     elif path[i]=="." and path[i+1]==".":
#         if len(stack)!=0:
#             stack.pop()
#
#     elif path[i]==".":
#         s=""
#     else:
#         s+=path[i]
# if len(stack)==0:
#     print("/")
# else:
#     a = ""
#     for j in stack:
#         a+="/"+j
#     print(a)
