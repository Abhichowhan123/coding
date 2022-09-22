class MyQueue:

    def __init__(self):
        self.stack = []
        self.id = 0
    def push(self, x: int) -> None:
        self.stack = self.stack+[x]
        # self.stack.append(x)
    def pop(self) -> int:
        self.id += 1
        if len(self.stack)!=0:
            return self.stack.pop(self.id - 1)
        else:
            return self.stack[self.id - 1]
    def peek(self) -> int:
        return self.stack[self.id]

    def empty(self) -> bool:
        if len(self.stack)==0:
            return True
        else:
            return  False
obj = MyQueue
obj.push(1)
obj.push(2)
q = obj.peek()
print(q)

# ["MyQueue","push","push","push","push","pop","push","pop","pop","pop","pop"]
# [[],[1],[2],[3],[4],[],[5],[],[],[],[]]