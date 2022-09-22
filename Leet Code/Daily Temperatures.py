temperatures = [89,62,70,58,47,47,46,76,100,70]
stack = []
A = [0]*len(temperatures)
count= 0
for i in range(len(temperatures)-1,-1,-1):
    while stack and stack[-1][0]<=temperatures[i]:
        stack.pop()
    if stack and stack[-1][0] > temperatures[i]:
        A[i] = abs((stack[-1][1]) - i)
        stack.append([temperatures[i], i])
    else:
        if len(stack) == 0:
            A[i] = 0
            stack.append([temperatures[i], i])
print(A)

































    # while stack and stack[-1]>[temperatures[i],i]:
    #     w = stack[-1][0]
    #     A[i]  =w-i
    #     stack.pop()
    # if len(stack)==0:
    #     stack.append([temperatures[i],i])
    #     A[i] = 0
    #
    # if stack and stack[-1]>[temperatures[i],i]:
    #
    # stack.append([temperatures[i],i])

