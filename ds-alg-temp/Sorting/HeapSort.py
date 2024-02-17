# Python program for implementation of heap Sort

# To heapify subtree rooted at index i.
# n is size of heap


def heapify(arr, n, i):
	largest = i # Initialize largest as root
	l = 2 * i + 1	 # left = 2*i + 1
	r = 2 * i + 2	 # right = 2*i + 2

	# See if left child of root exists and is
	# greater than root
	if l < n and arr[largest] < arr[l]:
		largest = l

	# See if right child of root exists and is
	# greater than root
	if r < n and arr[largest] < arr[r]:
		largest = r

	# Change root, if needed
	if largest != i:
		arr[i], arr[largest] = arr[largest], arr[i] # swap

		# Heapify the root.
		heapify(arr, n, largest)

# The main function to sort an array of given size


def heapSort(arr):
	n = len(arr)

	# Build a maxheap.
	for i in range(n//2 - 1, -1, -1):
		heapify(arr, n, i)

	# One by one extract elements
	for i in range(n-1, 0, -1):
		arr[i], arr[0] = arr[0], arr[i] # swap
		heapify(arr, i, 0)


# Driver code
arr = [12, 11, 13, 5, 6, 7]
heapSort(arr)
n = len(arr)
print("Sorted array is")
for i in range(n):
	print("%d" % arr[i]),
# This code is contributed by Mohit Kumra

# - heapify
#   - child가 더 크면 largest를 바꿈.
#   - largest가 바뀌었으면 swap, 이후 root를 다시 heapify.
#   - 정확한 동작을 이해하려면 항상 코드를 하나하나 그림으로 따라가보자.
#
# - 논리 코드:
#   - heapSort(A)
#     - buildHeap(A)
#     - for i = A.length downto 2
#       - swap(A[1],A[i])
#       - A.heap_size -= 1
#       - heapify(A,1)
#
# - 설명:
#   - 처음과 끝 원소 swap, 첫 원소 heapify.
#   - 다음 loop에서는 heap 크기 1 줄여서 생각.