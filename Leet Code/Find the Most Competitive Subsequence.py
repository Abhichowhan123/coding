nums =[2,4,3,3,5,4,9,6]
k = 4
stack = []
m = len(nums)-k
for i in nums:
    while stack and stack[-1]>i and m>0:
        m-=1
        stack.pop()
    stack.append(i)
print(stack[:k])





# nums =[71,18,52,29,55,73,24,42,66,8,80,2]
# k = 3
# d = k
# stack = []
# for i in nums:
#     if len(stack)== 0:
#         stack.append(i)
#         d-=1
#     else:
#         if d>0 and stack[-1]<i:
#             stack.append(i)
#             d-= 1
#         else:
#             while stack and stack[-1]>i:
#                 stack.pop()
#                 d+=1
#             if d > 0 :
#                 stack.append(i)
#                 d -= 1
# print(stack)