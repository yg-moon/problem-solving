# Python program for implementation of MergeSort
def mergeSort(arr):
	if len(arr) > 1: # 경계조건 확인

		# Finding the mid of the array
		mid = len(arr)//2

		# Dividing the array elements
		L = arr[:mid]

		# into 2 halves
		R = arr[mid:]

		# Sorting the first half
		mergeSort(L)

		# Sorting the second half
		mergeSort(R)

		i = j = k = 0

		# Copy data to temp arrays L[] and R[]
		while i < len(L) and j < len(R):
			if L[i] < R[j]:
				arr[k] = L[i]
				i += 1
			else:
				arr[k] = R[j]
				j += 1
			k += 1

		# Checking if any element was left
		while i < len(L):
			arr[k] = L[i]
			i += 1
			k += 1

		while j < len(R):
			arr[k] = R[j]
			j += 1
			k += 1

# Code to print the list


def printList(arr):
	for i in range(len(arr)):
		print(arr[i], end=" ")
	print()


# Driver Code
if __name__ == '__main__':
	arr = [12, 11, 13, 5, 6, 7]
	print("Given array is", end="\n")
	printList(arr)
	mergeSort(arr)
	print("Sorted array is: ", end="\n")
	printList(arr)

# This code is contributed by Mayank Khanna

# - merge()에서 end of list checking:
#     무조건 두 절반 중 하나는 다 옮긴 상태기 때문에, 두 while문 중 하나만 실행된다.
#     아직 다 못 옮긴 절반의 남은 원소들만 차례대로 복사하게 된다.
#
# - 기본 논리 코드:
# - mergeSort(A, start, end)
#   - if start < end:
#     - mid = floor((start+end)/2)
#     - mergeSort(A, start, mid)
#     - mergeSort(A, mid+1, end)
#     - merge(A, start, mid, end)