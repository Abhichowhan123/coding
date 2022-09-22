heights = [2,1,5,6,2,3]
m = 0
stack = []
for i,h in enumerate (heights):
    start =  i
    while stack and stack[-1][1]>h:
        index,height = stack.pop()
        m= max(m,height*(i-index))
        start = index
    stack.append((start,h))
for i ,h in stack:
    m  = max(m,h*(len(heights)-i))
print(m)











# Time Limit Exceeded
# heights =[2,4]
#
# left = []
# right= []
# for i in range(len(heights)):
#     r,l= 0,0
#     a,b = i,i
#     while (a>=0):
#         if heights[a]>=heights[i]:
#             l+=1
#             a-=1
#         else:
#             break
#     if l==0:
#         left.append(1)
#     else:
#         left.append(l)
#
#     while b!=len(heights):
#         if heights[b]>=heights[i]:
#             r+=1
#             b+=1
#         else:
#             break
#     if r==0:
#         right.append(1)
#     else:
#         right.append(r)
#
# # print(heights)
# # print("left",left)
# # print("right",right)
# # total = []
# count = 0
# # for j in range(len(heights)):
# #     total.append(((left[j]+right[j])*heights[j])-heights[j])
# # print(total)
# # count = 0
# for j in range(len(heights)):
#     count =  max(count,((left[j]+right[j])*heights[j])-heights[j])
# print(count)