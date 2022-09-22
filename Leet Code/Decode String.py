s = "3[a2[c]]"
stack = []
char = ""
num = ""
for i in s:
    if i!="]":
        stack.append(i)
    else:
        while stack[-1]!="[":
            char=stack.pop()+char
        stack.pop()
        while stack and stack[-1].isdigit():
            num=stack.pop()+num
        for j in range(int(num)):
            stack.append(char)
        char = ""
        num = ""
print("".join(stack))