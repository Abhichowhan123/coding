class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = []
        self.k = k
    def enQueue(self, value: int) -> bool:
        if len(self.queue)<self.k:
            self.queue.append(value)
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if len(self.queue)==0:
            return False

        deque_val = self.queue[0]
        del self.queue[0]
        return True

    def Front(self) -> int:
        if  len(self.queue)==0:
            return -1
        else:
            return self.queue[0]

    def Rear(self) -> int:
        if  len(self.queue)==0:
            return -1
        else:
            return self.queue[-1]

    def isEmpty(self) -> bool:
        if  len(self.queue)==0:
            return True
        else:
            return False
    def isFull(self) -> bool:
        if  len(self.queue)==self.k:
            return True
        else:
            return False

