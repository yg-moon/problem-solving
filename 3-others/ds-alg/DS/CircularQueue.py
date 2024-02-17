class CircularQueue():

	# constructor
	def __init__(self, size): # initializing the class
		self.size = size
		
		# initializing queue with none
		self.queue = [None for i in range(size)]
		self.front = self.rear = -1

	def enqueue(self, data):
		
		# condition if queue is full
		if ((self.rear + 1) % self.size == self.front):
			print(" Queue is Full\n")
			
		# condition for empty queue
		elif (self.front == -1):
			self.front = 0
			self.rear = 0
			self.queue[self.rear] = data
		else:
			
			# next position of rear
			self.rear = (self.rear + 1) % self.size
			self.queue[self.rear] = data
			
	def dequeue(self):
		if (self.front == -1): # condition for empty queue
			print ("Queue is Empty\n")
			
		# condition for only one element
		elif (self.front == self.rear):
			temp=self.queue[self.front]
			self.front = -1
			self.rear = -1
			return temp
		else:
			temp = self.queue[self.front]
			self.front = (self.front + 1) % self.size
			return temp

	def display(self):
	
		# condition for empty queue
		if self.front == -1:
			print ("Queue is Empty")

		elif self.rear >= self.front:
			print("Elements in the circular queue are:",
											end = " ")
			for i in range(self.front, self.rear + 1):
				print(self.queue[i], end = " ")
			print ()

		else:
			print ("Elements in Circular Queue are:",
										end = " ")
			for i in range(self.front, self.size):
				print(self.queue[i], end = " ")
			for i in range(0, self.rear + 1):
				print(self.queue[i], end = " ")
			print ()

		if ((self.rear + 1) % self.size == self.front):
			print("Queue is Full")

# Driver Code
ob = CircularQueue(5)
ob.enqueue(14)
ob.enqueue(22)
ob.enqueue(13)
ob.enqueue(-6)
ob.display()
print ("Deleted value = ", ob.dequeue())
print ("Deleted value = ", ob.dequeue())
ob.display()
ob.enqueue(9)
ob.enqueue(20)
ob.enqueue(5)
ob.display()

# This code is contributed by AshwinGoel

# - 사실 이전 것도 circular 구현이긴 하다.
# - 차이점:
#   - "현재 크기"를 나타내는 size 변수가 사라졌다.
#   - "전체 크기"가 capacity 대신 size 라는 이름으로 변경되었다.
#   - 이에 따라 isFull(), isEmpty() 함수가 사라졌고 다르게 구현되었다.
# - 구현:
#   - front = rear = -1 에서 시작하는 방법으로 예외를 확인.
#   - isFull() 확인: if(rear+1 == front)
#   - isEmpty() 확인: if(front == -1)
# - 예외처리:
#   - Enqueue(): empty 이면 front = rear = 0 으로 설정.
#   - Dequeue(): 하나만 남았으면 (front == rear 이면) front = rear = -1 으로 설정.
# - 소감:
#   - 기능적인 차이는 없는 것 같다. "현재 크기 변수" 하나로 얼마나 구현이 간단해질 수 
#     있는지 느꼈다.