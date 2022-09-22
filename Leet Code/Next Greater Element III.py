n = list(str(452654))
print(n)
stack = []
for i in range(len(n)-1,-1,-1):
    # while stack and stack[-1]<n[i]:
    #     stack.pop()
    # stack.append(n[i])
    if n[len(n)-1]>stack[-1]:
        pass

print(stack)
