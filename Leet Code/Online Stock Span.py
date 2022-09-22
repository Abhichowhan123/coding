num = [100,80,60,70,60,75,85]
stack = []
A = []
for i in range(len(num)):
    while stack and stack[-1][0]<num[i]:
        stack.pop()

    if stack and stack[-1][0]>num[i]:
        A.append(abs(stack[-1][1]-i))
        stack.append([num[i], i])
    else:
        if len(stack)==0:
            stack.append([num[i],i])
            A.append(1)


# class StockSpanner:
#
#     def __init__(self):
#         self.stack = []
#     def next(self, price: int) -> int:
#         span = 1
#         while self.stack and self.stack[-1][0]<= price:
#             span+=self.stack[-1][1]
#             self.stack.pop()
#         self.stack.append((price,span))
#         return span