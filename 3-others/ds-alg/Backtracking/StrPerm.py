# Python program to print all permutations with
# duplicates allowed

def toString(List):
	return ''.join(List)

# Function to print permutations of string
# This function takes three parameters:
# 1. String
# 2. Starting index of the string
# 3. Ending index of the string.
def permute(a, l, r):
	if l==r:
		print (toString(a))
	else:
		for i in range(l,r+1):
			a[l], a[i] = a[i], a[l]
			permute(a, l+1, r)
			a[l], a[i] = a[i], a[l] # backtrack

# Driver program to test the above function
string = "ABC"
n = len(string)
a = list(string)
permute(a, 0, n-1)

# This code is contributed by Bhavya Jain

# - 잘 이해가 안 될 때는 그림, 다이어그램 참고
# 
# - 구현:
#   - for 문: 앞 글씨를 고정시키는 용도
#   - 재귀 permute(): 고정된 글씨 빼고 다시 recursion 하는 용도.
#   - backtrack: 고정시킨 글씨 돌려놓기. (다음 for문에서 다른 글씨를 고정시키기 위함.)
