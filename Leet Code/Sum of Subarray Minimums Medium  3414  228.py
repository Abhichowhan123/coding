arr = [3,1,2,4]
left = [1]*len(arr)
stack = [(arr[0],1)]
for i in range(1,len(arr)):
    while stack and arr[i]<=stack[-1][0]:
        left[i] +=stack.pop()[1]
    stack.append((arr[i],left[i]))
right = [1]*len(arr)
stack = [(arr[-1],1)]
for i in range(len(arr)-2,-1,-1):
    while stack and arr[i]<stack[-1][0]:
        right[i]+=stack.pop()[1]
    stack.append((arr[i],right[i]))
count = 0
for i in range(len(arr)):
    count+=arr[i]*left[i]*right[i]

print(count%(10**9+7))