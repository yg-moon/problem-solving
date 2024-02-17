# Python3 code to implement Jump Search
import math

def jumpSearch( arr , x , n ):
	
	# Finding block size to be jumped
	step = math.sqrt(n)
	
	# Finding the block where element is
	# present (if it is present)
	prev = 0
	while arr[int(min(step, n)-1)] < x:
		prev = step
		step += math.sqrt(n)
		if prev >= n:
			return -1
	
	# Doing a linear search for x in
	# block beginning with prev.
	while arr[int(prev)] < x:
		prev += 1
		
		# If we reached next block or end
		# of array, element is not present.
		if prev == min(step, n):
			return -1
	
	# If element is found
	if arr[int(prev)] == x:
		return prev
	
	return -1

# Driver code to test function
arr = [ 0, 1, 1, 2, 3, 5, 8, 13, 21,
	34, 55, 89, 144, 233, 377, 610 ]
x = 55
n = len(arr)

# Find the index of 'x' using Jump Search
index = jumpSearch(arr, x, n)

# Print the index where 'x' is located
print("Number" , x, "is at index" ,"%.0f"%index)

# This code is contributed by "Sharad_Bhardwaj".

# - Sorted Array를 가정한다는 것이 중요하다.
#
# - 두 개의 커서를 사용한다.
#   - prev: x가 있는 블럭 시작점까지 와서, 한 칸씩 전진한다.
#   - step: 블럭 단위로 건너뛰며, x가 있는 블럭 끝지점에 선다.
#
# - 정확한 구현 이해하기
#   - 값이 변하는 시점을 확인한다. (코드 순서)
#   - critical moment에서 해당 index들이 무슨 역할을 하는지 확인한다. (직접 돌려보기)
