arr = [2,1,3,4,4]
count=1
A=[]
mi=999999999
for item in arr[::-1]:
    A.append(min(mi,item))
    mi=min(mi,item)
A = A[::-1]
temp=0
for i in range(len(arr)-1):
    temp=max(temp,arr[i])
    if temp<=A[i+1]:
        temp=0
        count+=1
print(count)














# stack = []
# count =1
# for  i in range(len(arr)):
#     if stack and stack[-1]<=arr[i]:
#         while len(stack)!=0:
#             stack.pop()
#         count+=1
#         stack.append(arr[i])
#     else:
#         stack.append(arr[i])
# print(count)