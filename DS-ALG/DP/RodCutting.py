# A Dynamic Programming solution for Rod cutting problem
INT_MIN = -32767

# Returns the best obtainable price for a rod of length n and
# price[] as prices of different pieces
def cutRod(price, n):
	val = [0 for x in range(n+1)]
	val[0] = 0

	# Build the table val[] in bottom up manner and return
	# the last entry from the table
	for i in range(1, n+1):
		max_val = INT_MIN
		for j in range(i):
			max_val = max(max_val, price[j] + val[i-j-1])
		val[i] = max_val

	return val[n]

# Driver program to test above functions
arr = [1, 5, 8, 9, 10, 17, 17, 20]
size = len(arr)
print("Maximum Obtainable Value is " + str(cutRod(arr, size)))

# This code is contributed by Bhavya Jain

# - 1차원 배열로 해결되는 문제
#   - val[n]: 길이 n인 rod를 잘라 얻는 최고의 가격
#   - i: 임시 rod 길이
#     - j: 임시 rod를 자른 위치
#   - 매 i 마다, 모든 j를 시도하고, 그 중 최고 가격이 val[i]에 저장됨

# - Recursive Version
# def cutRod(price, n):
# 	if(n <= 0):
# 		return 0
# 	max_val = -sys.maxsize-1
#
# 	for i in range(0, n):
# 		max_val = max(max_val, price[i] +
# 					cutRod(price, n - i - 1))
# 	return max_val