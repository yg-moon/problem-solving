# Solution using two queues.

class MyStack:
    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, x: int) -> None:
        if self.queue1:
            self.queue1.append(x)
        else:
            self.queue2.append(x)

    def pop(self) -> int:
        if self.queue1:
            for _ in range(len(self.queue1) - 1):
                self.queue2.append(self.queue1.pop(0))
            return self.queue1.pop(0)
        elif self.queue2:
            for _ in range(len(self.queue2) - 1):
                self.queue1.append(self.queue2.pop(0))
            return self.queue2.pop(0)

    def top(self) -> int:
        if self.queue1:
            for _ in range(len(self.queue1) - 1):
                self.queue2.append(self.queue1.pop(0))
            top = self.queue1.pop(0)
            self.queue2.append(top)
            return top
        elif self.queue2:
            for _ in range(len(self.queue2) - 1):
                self.queue1.append(self.queue2.pop(0))
            top = self.queue2.pop(0)
            self.queue1.append(top)
            return top

    def empty(self) -> bool:
        if not self.queue1 and not self.queue2:
            return True
        else:
            return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
