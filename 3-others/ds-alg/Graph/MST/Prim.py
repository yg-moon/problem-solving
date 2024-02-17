# A Python program for Prim's Minimum Spanning Tree (MST) algorithm.
# The program is for adjacency matrix representation of the graph

import sys # Library for INT_MAX

class Graph():

	def __init__(self, vertices):
		self.V = vertices
		self.graph = [[0 for column in range(vertices)]
					for row in range(vertices)]

	# A utility function to print the constructed MST stored in parent[]
	def printMST(self, parent):
		print ("Edge \tWeight")
		for i in range(1, self.V):
			print (parent[i], "-", i, "\t", self.graph[i][ parent[i] ])

	# A utility function to find the vertex with
	# minimum distance value, from the set of vertices
	# not yet included in shortest path tree
	
	# ExtractMin
	def minKey(self, key, mstSet):

		# Initialize min value
		min = sys.maxsize

		for v in range(self.V):
			if key[v] < min and mstSet[v] == False:
				min = key[v]
				min_index = v

		return min_index

	# Function to construct and print MST for a graph
	# represented using adjacency matrix representation
	def primMST(self):

		# Key values used to pick minimum weight edge in cut
		key = [sys.maxsize] * self.V
		parent = [None] * self.V # Array to store constructed MST
		# Make key 0 so that this vertex is picked as first vertex
		key[0] = 0
		mstSet = [False] * self.V

		parent[0] = -1 # First node is always the root of

		for cut in range(self.V):

			# Pick the minimum distance vertex from
			# the set of vertices not yet processed.
			# u is always equal to src in first iteration
			u = self.minKey(key, mstSet)

			# Put the minimum distance vertex in
			# the shortest path tree
			mstSet[u] = True

			# Update dist value of the adjacent vertices
			# of the picked vertex only if the current
			# distance is greater than new distance and
			# the vertex in not in the shotest path tree
			for v in range(self.V):

				# graph[u][v] is non zero only for adjacent vertices of m
				# mstSet[v] is false for vertices not yet included in MST
				# Update the key only if graph[u][v] is smaller than key[v]
				
				# Relaxation
				if self.graph[u][v] > 0 and mstSet[v] == False and \
					key[v] > self.graph[u][v]:
						key[v] = self.graph[u][v]
						parent[v] = u

		self.printMST(parent)

g = Graph(5)
g.graph = [ [0, 2, 0, 6, 0],
			[2, 0, 3, 8, 5],
			[0, 3, 0, 0, 7],
			[6, 8, 0, 0, 9],
			[0, 5, 7, 9, 0]]

g.primMST()

# Contributed by Divyanshu Mehta

# - 변수:
#   - key[]: 각 vertex들 weight 배열.
#   - mstSet[]: 집합 S 포함 여부 확인 배열. (True/False)
#   - parent[]: 최종 MST.
# - 구현:
#   - "extractMin, include in set S, relaxation"의 반복.
#
#     - 각 구현의 핵심은 if문 조건과 이후 동작.
#
#   - 결국 weight는 첫 graph 배열에서, 연결 관계는 parent 배열에서 가져온다.
# - 분석 방법:
#   - 1. 최종 결과가 어디에서 나오는지 파악.
#   - 2. 각 변수가 무엇을 뜻하는지 파악.
#   - 3. 전체 구현을 이해.
#   - 4. 세부 구현을 이해.