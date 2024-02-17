# Python3 Program to print BFS traversal
# from a given source vertex. BFS(int s)
# traverses vertices reachable from s.
from collections import defaultdict

# This class represents a directed graph
# using adjacency list representation
class Graph:

	# Constructor
	def __init__(self):

		# default dictionary to store graph
		self.graph = defaultdict(list)

	# function to add an edge to graph
	def addEdge(self,u,v):
		self.graph[u].append(v)

	# Function to print a BFS of graph
	def BFS(self, s):

		# Mark all the vertices as not visited
		visited = [False] * (max(self.graph) + 1)

		# Create a queue for BFS
		queue = []

		# Mark the source node as
		# visited and enqueue it
		queue.append(s)
		visited[s] = True

		while queue:

			# Dequeue a vertex from
			# queue and print it
			s = queue.pop(0)
			print (s, end = " ")

			# Get all adjacent vertices of the
			# dequeued vertex s. If a adjacent
			# has not been visited, then mark it
			# visited and enqueue it
			for i in self.graph[s]:
				if visited[i] == False:
					queue.append(i)
					visited[i] = True

# Driver code

# Create a graph given in
# the above diagram
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(5, 3)

print ("Following is Breadth First Traversal"
				" (starting from vertex 2)")
g.BFS(2)

# This code is contributed by Neelam Yadav

# - Python 관련:
#   - List representation: defaultdict() 이용.
#   - defaultdict(): KeyError 가 없음.
#   - dict의 max는 '최대 key값'을 의미한다. (value값 아님) (열심히 디버깅으로 찾아냄)
#
# - Enqueue, Dequeue는 append(), pop() 으로 구현.
#   - Dequeue 이후 인접 노드 전부 Enqueue 하는 것이 핵심.
#   - pop()은 기본적으로 마지막 원소를 주기 때문에, pop(0) 으로 맨 앞에서 꺼냄.
