# Program to find if there is a simple path with
# weight more than k

# This class represents a dipathted graph using
# adjacency list representation
class Graph:
	# Allocates memory for adjacency list
	def __init__(self, V):
		self.V = V
		self.adj = [[] for i in range(V)]

	# Returns true if graph has path more than k length
	def pathMoreThanK(self,src, k):
		# Create a path array with nothing included
		# in path
		path = [False]*self.V
	
		# Add source vertex to path
		path[src] = 1
	
		return self.pathMoreThanKUtil(src, k, path)
	
	# Prints shortest paths from src to all other vertices
	def pathMoreThanKUtil(self, src, k, path):
		# If k is 0 or negative, return true
		if (k <= 0):
			return True
	
		# Get all adjacent vertices of source vertex src and
		# recursively explore all paths from src.
		i = 0
		while i != len(self.adj[src]):
			# Get adjacent vertex and weight of edge
			v = self.adj[src][i][0]
			w = self.adj[src][i][1]
			i += 1
	
			# If vertex v is already there in path, then
			# there is a cycle (we ignore this edge)
			if (path[v] == True):
				continue
	
			# If weight of is more than k, return true
			if (w >= k):
				return True
	
			# Else add this vertex to path
			path[v] = True
	
			# If this adjacent can provide a path longer
			# than k, return true.
			if (self.pathMoreThanKUtil(v, k-w, path)):
				return True
	
			# 그것도 아니라면, Backtrack
			path[v] = False
	
		# If no adjacent could produce longer path, return
		# false
		return False
	
	# Utility function to an edge (u, v) of weight w
	def addEdge(self,u, v, w):
		self.adj[u].append([v, w])
		self.adj[v].append([u, w])

# Driver program to test methods of graph class
if __name__ == '__main__':

	# create the graph given in above fugure
	V = 9
	g = Graph(V)

	# making above shown graph
	g.addEdge(0, 1, 4)
	g.addEdge(0, 7, 8)
	g.addEdge(1, 2, 8)
	g.addEdge(1, 7, 11)
	g.addEdge(2, 3, 7)
	g.addEdge(2, 8, 2)
	g.addEdge(2, 5, 4)
	g.addEdge(3, 4, 9)
	g.addEdge(3, 5, 14)
	g.addEdge(4, 5, 10)
	g.addEdge(5, 6, 2)
	g.addEdge(6, 7, 1)
	g.addEdge(6, 8, 6)
	g.addEdge(7, 8, 7)

	src = 0
	k = 62
	if g.pathMoreThanK(src, k):
		print("Yes")
	else:
		print("No")

	k = 60
	if g.pathMoreThanK(src, k):
		print("Yes")
	else:
		print("No")

# - 구현:
#   - 여태 진행한걸 path에 저장하고 (path[vertex] = True)
#   - 그 지점부터 다시 재귀로 계산. if (self.pathMoreThanKUtil(v, k-w, path))
#   - 결과가 안 나오면 backtrack. (path[vertex] = False)

# - Util을 이용하는 이유: 상위 함수에서 만든 지역변수 path[]를 이용하기 위해.
# - 특정 조건이 만족할 때 까지 반복: while문이 적합.