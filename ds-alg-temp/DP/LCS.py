# Dynamic Programming implementation of LCS problem

def lcs(X , Y):
	# find the length of the strings
	m = len(X)
	n = len(Y)

	# declaring the array for storing the dp values
	L = [[None]*(n+1) for i in range(m+1)]

	"""Following steps build L[m+1][n+1] in bottom up fashion
	Note: L[i][j] contains length of LCS of X[0..i-1]
	and Y[0..j-1]"""
	for i in range(m+1):
		for j in range(n+1):
			if i == 0 or j == 0 :
				L[i][j] = 0
			elif X[i-1] == Y[j-1]:
				L[i][j] = L[i-1][j-1]+1
			else:
				L[i][j] = max(L[i-1][j] , L[i][j-1])

	# L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
	return L[m][n]
#end of function lcs


# Driver program to test the above function
X = "AGGTAB"
Y = "GXTXAYB"
print ("Length of LCS is ", lcs(X, Y))

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)

# - L[m][n] 에서 m은 세로, n은 가로.
#
# - Optimal substructure를 알아야 풀 수 있고 이해할 수 있다.
#   - If last characters of both sequences match (or X[m-1] == Y[n-1]) then 
#     L(X[0..m-1], Y[0..n-1]) = 1 + L(X[0..m-2], Y[0..n-2])
#     If last characters of both sequences do not match (or X[m-1] != Y[n-1]) then 
#     L(X[0..m-1], Y[0..n-1]) = MAX ( L(X[0..m-2], Y[0..n-1]), L(X[0..m-1], Y[0..n-2]))
#
# - 이에 따르면 재귀로 풀어낸 코드는
#
# def lcs(X, Y, m, n):
#     if m == 0 or n == 0:
#     return 0;
#     elif X[m-1] == Y[n-1]:
#     return 1 + lcs(X, Y, m-1, n-1);
#     else:
#     return max(lcs(X, Y, m, n-1), lcs(X, Y, m-1, n));
# X = "AGGTAB"
# Y = "GXTXAYB"
# print "Length of LCS is ", lcs(X , Y, len(X), len(Y))
#
# - 이걸 바탕으로 tabulation 하면 됨.
