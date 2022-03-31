class MyCircularQueue:
    def __init__(self, k: int):
        self.q = [None] * k
        self.max_len = k
        self.curr_size = 0
        self.front = 0
        self.rear = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.q[self.rear] = value
            self.curr_size += 1
            # Method1: % operator
            self.rear = (self.rear + 1) % self.max_len
            return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.q[self.front] = None
            self.curr_size -= 1
            self.front += 1
            # Method2: classic way
            if self.front == self.max_len:
                self.front = 0
            return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.q[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.q[self.rear - 1]

    def isEmpty(self) -> bool:
        if self.curr_size == 0:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if self.curr_size == self.max_len:
            return True
        else:
            return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
