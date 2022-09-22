from collections import deque
class RecentCounter:

    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        w = t-3000
        while self.queue and self.queue[-1]<w:
            self.queue.pop()
        self.queue.appendleft(t)
        return len(self.queue)

A  = RecentCounter()
w = A.ping(1)
q = A.ping(2)
e = A.ping(100)
r = A.ping(1)
t = A.ping(1)
y = A.ping(1)
u = A.ping(1)

