directions = "SSRSSRLLRSLLRSRSSRLRRRRLLRRLSSRR"
stack = []
count = 0
for i in directions:
    if len(stack)==0 and i=="L":
        continue
    else:
        if i== "L":
            if stack and stack[-1]=="R":
                count+=2
                stack.pop()
                while stack and stack[-1]=="R":
                    stack.pop()
                    count+=1
            elif stack and stack[-1]=="S":
                count+=1
            stack.append("S")
        elif i=="R":
            stack.append("R")
        elif i=="S":
            while stack and stack[-1]=="R":
                count+=1
                stack.pop()
            stack.append("S")
print(count)

