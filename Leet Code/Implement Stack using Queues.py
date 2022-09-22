from collections import deque


class MyStack:

    def __init__(self):
        self.Q = deque()
    def push(self, x: int) -> None:
        self.Q.append(x)
    def pop(self) -> int:
        for i in range(len(self.Q)-1):
            self.push(self.Q.popleft())
        return self.Q.popleft()
    def top(self) -> int:
        return self.Q[-1]
    def empty(self) -> bool:
        return len(self.Q)==0


