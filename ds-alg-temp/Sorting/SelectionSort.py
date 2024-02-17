# Python program for implementation of Selection
# Sort
import sys

def selectionSort(A):
	# Traverse through all array elements
	for i in range(len(A)):
		
		# Find the minimum element in remaining
		# unsorted array
		min_idx = i
		for j in range(i+1, len(A)):
			if A[min_idx] > A[j]:
				min_idx = j
				
		# Swap the found minimum element with
		# the first element	
		A[i], A[min_idx] = A[min_idx], A[i]
	return A

# Driver code to test above
print ("Sorted array")
B = [64, 25, 12, 22, 11]
selectionSort(B)

for i in range(len(B)):
	print("%d" %B[i])

# - 구조: min element 찾고, swap.
#   - comparison은 min element 찾을 때 일어난다.
#   - swap은 매 loop마다 딱 1회만 발생한다.