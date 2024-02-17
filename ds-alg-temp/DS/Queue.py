# Python3 program for array implementation of queue

# Class Queue to represent a queue
class Queue:
    def __init__(self, capacity):
        self.Q = [None] * capacity
        self.capacity = capacity
        self.size = 0
        self.front = 0
        self.rear = capacity - 1

    # Queue is full when size becomes
    # equal to the capacity
    def isFull(self):
        return self.size == self.capacity

    # Queue is empty when size is 0
    def isEmpty(self):
        return self.size == 0

    # Function to add an item to the queue.
    # It changes rear and size
    def EnQueue(self, item):
        if self.isFull():
            print("Full")
            return
        self.rear = (self.rear + 1) % (self.capacity)
        self.Q[self.rear] = item
        self.size = self.size + 1
        print("% s enqueued to queue" % str(item))

    # Function to remove an item from queue.
    # It changes front and size
    def DeQueue(self):
        if self.isEmpty():
            print("Empty")
            return

        print("% s dequeued from queue" % str(self.Q[self.front]))
        self.front = (self.front + 1) % (self.capacity)
        self.size = self.size - 1

    # Function to get front of queue
    def que_front(self):
        if self.isEmpty():
            print("Queue is empty")

        print("Front item is", self.Q[self.front])

    # Function to get rear of queue
    def que_rear(self):
        if self.isEmpty():
            print("Queue is empty")
        print("Rear item is", self.Q[self.rear])


# Driver Code
if __name__ == "__main__":

    queue = Queue(30)
    queue.EnQueue(10)
    queue.EnQueue(20)
    queue.EnQueue(30)
    queue.EnQueue(40)
    queue.DeQueue()
    queue.que_front()
    queue.que_rear()

# - Circular Queue 구현: rear나 front에 +1 이후, % capacity를 해줌.
#
# - 핵심: Enqueue는 rear, Dequeue는 front에서 이루어짐. (그냥 매장 대기열과 동일)
# 	- 구현 차이: 지금 코드는 rear가 맨 끝에서 시작하기 때문에 idx+1 이후에
#     insert를 해야 하지만, front=rear=0 인 구현에서는 insert 이후에 idx+1을 한다.
#     (실행 순서가 다르다)
#
# - 이해가 안 될 땐 그림을 그리자! (항상 성공한 방법. 이번에도 성공.)
#
# - 코드의 정확한 동작을 이해하려면, idx에 따른 정확한 상태변화를 따라갈 수 있어야.
