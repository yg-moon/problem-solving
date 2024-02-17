# 3.5 Sort Stacks
import unittest

from chapter_03.stack import Stack


class SortedStack2(Stack):
    def __init__(self):
        super().__init__()
        self.temp_stack = Stack()

    def push(self, item):
        if self.is_empty() or item < self.peek():
            super().push(item)
        else:
            while self.peek() is not None and item > self.peek():
                self.temp_stack.push(self.pop())
            super().push(item)
            while not self.temp_stack.is_empty():
                super().push(self.temp_stack.pop())


# Sol1. 입력이 고정된 경우
def my_sol(stack1):
    if not stack1:
        return

    stack2 = []

    while stack1:
        cur = stack1.pop()
        cnt = 0

        while stack2 and stack2[-1] < cur:
            stack1.append(stack2.pop())
            cnt += 1

        stack2.append(cur)

        for _ in range(cnt):
            stack2.append(stack1.pop())

    return stack2


# print(my_sol([1, 7, 4, 2, 3, 5, 6]))


# Sol2. 입력이 변하는 경우
class SortedStack:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, val):
        if not self.stack1:
            self.stack1.append(val)
        else:
            while self.stack1 and self.stack1[-1] < val:
                self.stack2.append(self.stack1.pop())
            self.stack1.append(val)
            while self.stack2:
                self.stack1.append(self.stack2.pop())

    def pop(self):
        return self.stack1.pop()

    def __len__(self):
        return len(self.stack1)


class Tests(unittest.TestCase):
    def test_push_one(self):
        queue = SortedStack()
        queue.push(1)
        assert len(queue) == 1

    def test_push_two(self):
        queue = SortedStack()
        queue.push(1)
        queue.push(2)
        assert len(queue) == 2

    def test_push_three(self):
        queue = SortedStack()
        queue.push(1)
        queue.push(2)
        queue.push(3)
        assert len(queue) == 3

    def test_pop_one(self):
        queue = SortedStack()
        queue.push(1)
        assert queue.pop() == 1

    def test_pop_two(self):
        queue = SortedStack()
        queue.push(1)
        queue.push(2)
        assert queue.pop() == 1
        assert queue.pop() == 2

    def test_pop_three(self):
        queue = SortedStack()
        queue.push(1)
        queue.push(2)
        queue.push(3)
        assert queue.pop() == 1
        assert queue.pop() == 2
        assert queue.pop() == 3

    def test_push_mixed(self):
        queue = SortedStack()
        queue.push(3)
        queue.push(2)
        queue.push(1)
        queue.push(4)
        assert queue.pop() == 1
        assert queue.pop() == 2
        assert queue.pop() == 3
        assert queue.pop() == 4


if __name__ == "__main__":
    unittest.main()
