# Python program for implementation of Insertion Sort

# Function to do insertion sort
def insertionSort(arr):

    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# Driver code to test above
arr = [12, 11, 13, 5, 6]
insertionSort(arr)
for i in range(len(arr)):
    print("% d" % arr[i])

# This code is contributed by Mohit Kumra

# - 요약: 한칸씩 오른쪽으로 올려주고, 마지막 자리에 key를 넣는 방식.
# - 구현:
#   - (i = 1) 부터 시작, (j = i-1) 이다.
#   - loop 동안은 arr[j+1]의 값만 업데이트하고, j -= 1.
#   - loop 종료 후 arr[j+1] = key 로 'insert' 해준다.
#
# - Python += 연산자
#   - i = i+1 보다 i += 1 이 더 효율적이다.
#   - 전자는 reassigment, 후자는 in-place로 교체하기 때문이다.
