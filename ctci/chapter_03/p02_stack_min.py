from chapter_03.stack import Stack


class MinStack(Stack):
    def __init__(self):
        super().__init__()
        self.minvals = Stack()

    def push(self, value):
        super().push(value)
        if not self.minvals or value <= self.get_min():
            self.minvals.push(value)

    def pop(self):
        value = super().pop()
        if value == self.get_min():
            self.minvals.pop()
        return value

    def get_min(self):
        return self.minvals.peek()


class MySol:
    def __init__(self):
        self.stack = []

    def push(self, val):
        cur_min = self.get_min() if self.get_min() else int(1e9)
        self.stack.append((val, min(cur_min, val)))  # (현재값, 최솟값)

    def pop(self):
        self.stack.pop()[0]

    def get_min(self):
        return self.stack[-1][1] if self.stack else None


def test_min_stack():
    # newstack = MinStack()
    newstack = MySol()
    assert newstack.get_min() is None

    newstack.push(5)
    assert newstack.get_min() == 5

    newstack.push(6)
    assert newstack.get_min() == 5

    newstack.push(3)
    assert newstack.get_min() == 3

    newstack.push(7)
    assert newstack.get_min() == 3

    newstack.push(3)
    assert newstack.get_min() == 3

    newstack.pop()
    assert newstack.get_min() == 3

    newstack.pop()
    assert newstack.get_min() == 3

    newstack.pop()
    assert newstack.get_min() == 5

    newstack.push(1)
    assert newstack.get_min() == 1


if __name__ == "__main__":
    test_min_stack()
