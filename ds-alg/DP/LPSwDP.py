# A Dynamic Programming based Python
# program for LPS problem Returns the length
# of the longest palindromic subsequence in seq
def lps(str):
	n = len(str)

	# Create a table to store results of subproblems
	L = [[0 for x in range(n)] for x in range(n)]

	# Strings of length 1 are palindrome of length 1
	for i in range(n):
		L[i][i] = 1

	for cl in range(2, n+1):
		for i in range(n-cl+1):
			j = i+cl-1
			if str[i] == str[j] and cl == 2:
				L[i][j] = 2
			elif str[i] == str[j]:
				L[i][j] = L[i+1][j-1] + 2
			else:
				L[i][j] = max(L[i][j-1], L[i+1][j])

	return L[0][n-1]

# Driver program to test above functions
seq = "GEEKSFORGEEKS"
n = len(seq)
print("The length of the LPS is " + str(lps(seq)))

print("haha")
# This code is contributed by Bhavya Jain

# - DP 문제들은 디버깅 모드에서 배열의 상태변화를 직접 보면 이해하기 더 쉽다.
#   - 배열의 대각선을 1로 채운 후, 우측 삼각형만 값 계산에 사용한다.
#   - MatChainMul과 같은 for문 논리를 사용
#     - L[m][n] = str[m...n] 에서 LPS의 길이
#     - cl: substring의 길이
#     - i: 시작지점
#     - j: 끝 지점

# - Optimal Substructure 식만 정확히 세울 수 있다면 나머지는 구현의 문제.