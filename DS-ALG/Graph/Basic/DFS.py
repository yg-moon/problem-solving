# Python program to print DFS
# traversal for complete graph
from collections import defaultdict

# This class represents a
# directed graph using adjacency
# list representation


class Graph:

	# Constructor
	def __init__(self):

		# default dictionary to store graph
		self.graph = defaultdict(list)

	# function to add an edge to graph
	def addEdge(self, u, v):
		self.graph[u].append(v)

	# A function used by DFS
	def DFSUtil(self, v, visited):

		# Mark the current node as visited and print it
		visited.add(v)
		print (v)

		# Recur for all the vertices adjacent to
		# this vertex
		for neighbour in self.graph[v]:
			if neighbour not in visited:
				self.DFSUtil(neighbour, visited)

	# The function to do DFS traversal. It uses
	# recursive DFSUtil()

	def DFS(self):

		# Create a set to store all visited vertices
		visited = set()

		# Call the recursive helper function to print
		# DFS traversal starting from all vertices one
		# by one
		for vertex in list(self.graph):
			if vertex not in visited:
				self.DFSUtil(vertex, visited)


# Driver code
# Create a graph given in the above diagram
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print ("Following is Depth First Traversal")
g.DFS()

# This code is contributed by Neelam Yadav

# - Python: list(dictionary object)를 하면 key만 list로 바뀐다. (item은 무시)

# - 구현:
#   - helper function 구조를 사용.
#   - 중요: disconnected graph 문제를 해결하기 위해 visited set을 검사.
