# Dynamic Programming Python implementation of Min Cost Path
# problem
R = 3
C = 3

def minCost(cost, m, n):
	tc = [[0 for x in range(C)] for x in range(R)]
	tc[0][0] = cost[0][0]

	# Initialize first column of total cost(tc) array
	for i in range(1, m+1):
		tc[i][0] = tc[i-1][0] + cost[i][0]

	# Initialize first row of tc array
	for j in range(1, n+1):
		tc[0][j] = tc[0][j-1] + cost[0][j]

	# Construct rest of the tc array
	for i in range(1, m+1):
		for j in range(1, n+1):
			tc[i][j] = min(tc[i-1][j-1], tc[i-1][j], tc[i][j-1]) + cost[i][j]

	return tc[m][n]

# Driver program to test above functions
cost = [[1, 2, 3],
		[4, 8, 2],
		[1, 5, 3]]
print(minCost(cost, 2, 2))

# This code is contributed by Bhavya Jain

# - 설명:
#   - 행렬에서 우, 하, 대각우하 로만 이동 가능한 상황에서 최소경로를 찾는 문제
#   - 따라서 이전 경로는 상, 좌, 대각좌상만 가능함
# - 구현:
#   - 첫 행과 첫 열만 cost 내용으로 초기화
#   - 나머지는 optimal substructure 이용
