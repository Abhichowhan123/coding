from collections import deque
class ProductOfNumbers:

    def __init__(self):
        self.stack = [1]
    def add(self, num: int) -> None:
        if num==0:
            self.stack = [1]
        else:
            self.stack.append(self.stack[-1]*num)
    def getProduct(self, k: int) -> int:
        if len(self.stack)-1 >=k:
            s = self.stack[-1]//self.stack[len(self.stack)-1-k]
            return s
        else:
            return 0
# class ProductOfNumbers:
#
#     def __init__(self):
#
#     def add(self, num: int) -> None:
#
#     def getProduct(self, k: int) -> int: