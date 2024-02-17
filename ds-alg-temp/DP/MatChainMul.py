# Dynamic Programming Python implementation of Matrix
# Chain Multiplication. See the Cormen book for details
# of the following algorithm
import sys

# Matrix Ai has dimension p[i-1] x p[i] for i = 1..n


def MatrixChainOrder(p, n):
	# For simplicity of the program,
	# one extra row and one
	# extra column are allocated in m[][].
	# 0th row and 0th
	# column of m[][] are not used
	m = [[0 for x in range(n)] for x in range(n)]

	# m[i, j] = Minimum number of scalar
	# multiplications needed
	# to compute the matrix A[i]A[i + 1]...A[j] =
	# A[i..j] where
	# dimension of A[i] is p[i-1] x p[i]

	# cost is zero when multiplying one matrix.
	for i in range(1, n):
		m[i][i] = 0

	# L is chain length.
	for L in range(2, n):
		for i in range(1, n-L + 1):
			j = i + L-1
			m[i][j] = sys.maxsize
			for k in range(i, j):

				# q = cost / scalar multiplications
				q = m[i][k] + m[k + 1][j] + p[i-1]*p[k]*p[j]
				if q < m[i][j]:
					m[i][j] = q

	return m[1][n-1]


# Driver code
arr = [1, 2, 3, 4]
size = len(arr)

print("Minimum number of multiplications is " +
	str(MatrixChainOrder(arr, size)))
# This Code is contributed by Bhavya Jain

# - 역시 책을 찾으니 이해가 쉽다. 까먹었으면 책을 보자.
#
# - 핵심1: Optimal Substructure
#   - min(A_i,j) = min(A_i,k) + min(A_k+1,j) + p_i-1 * p_k * p_j
#   - 행렬을 맘대로 둘로 나누고, 그 둘을 곱하는 비용까지 더하면 됨.
#
# - 핵심2: for문 논리
#   - L: 체인 길이 (행렬을 몇 개씩 묶을건지)
#   - i : 시작 지점 (range(1, n-L): 전체 길이 - 체인 길이 범위 내)
#   - j : 끝 지점 (i + L: 시작 지점 + 체인 길이)
#   - k : 시작 지점과 끝 지점 사이 임의의 점 (range(i, j) : 여기서 분할 시도)
#
# - 핵심3: 변수의 뜻을 명확히 알고 사용
#    - m[i][j]: A_i...j 를 곱하는 최소 비용.
#    - 따라서 return m[1][n-1]을 해야 A_1...n-1 까지 곱하는 비용의 최소가 됨.
