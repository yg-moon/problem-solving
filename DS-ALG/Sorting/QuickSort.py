# Python3 implementation of QuickSort

# This Function handles sorting part of quick sort
# start and end points to first and last element of
# an array respectively
def partition(start, end, array):

    # Initializing pivot's index to start
    pivot_index = start
    pivot = array[pivot_index]

    # This loop runs till start pointer crosses
    # end pointer, and when it does we swap the
    # pivot with element on end pointer
    while start < end:

        # Increment the start pointer till it finds an
        # element greater than pivot
        while start < len(array) and array[start] <= pivot:
            start += 1

        # Decrement the end pointer till it finds an
        # element less than pivot
        while array[end] > pivot:
            end -= 1

        # If start and end have not crossed each other,
        # swap the numbers on start and end
        if start < end:
            array[start], array[end] = array[end], array[start]

    # Swap pivot element with element on end pointer.
    # This puts pivot on its correct sorted place.
    array[end], array[pivot_index] = array[pivot_index], array[end]

    # Returning end pointer to divide the array into 2
    return end


# The main function that implements QuickSort
def quick_sort(start, end, array):

    if start < end:

        # p is partitioning index, array[p]
        # is at right place
        p = partition(start, end, array)

        # Sort elements before partition
        # and after partition
        quick_sort(start, p - 1, array)
        quick_sort(p + 1, end, array)


# Driver code
array = [10, 7, 8, 9, 1, 5]
quick_sort(0, len(array) - 1, array)

print(f"Sorted array: {array}")

# This code is contributed by Adnan Aliakbar

# - QuickSort 코드는 그냥 자동으로 튀어나올 때까지 익숙해지기.
#   - quickSort(A, start, end)
#     - if start < end:
#       - p = partition
#       - quickSort(A, start, p-1)
#       - quickSort(A, p+1, end)
#
# - partition:
#   - Python 버전은 코드가 조금 다르다.
#     - 개념:
#       - pivot은 맨 처음 원소.
#       - 왼쪽에서 pivot보다 큰 걸 찾고, 오른쪽에서 pivot보다 작은걸 찾아 계속 swap.
#       - start > end 가 될 때, swap(A[end],A[pivot]) 하면 끝.
#
#   - 원래 버전(C++, Java)
#     - 개념: 작은 걸 찾아 계속 왼쪽으로 보내다가, 마지막에 pivot을 중간에 놓는 방식.
#
#     - Java 코드
#       static int partition(int[] arr, int low, int high){
#           int pivot = arr[high];
#           int i = (low - 1); // 주의!
#           for(int j = low; j <= high-1; j++) {
#               if (arr[j] < pivot) {
#                   i++;
#                   swap(arr, i, j);
#               }
#           }
#           swap(arr, i + 1, high);
#           return (i + 1);
#       }
#
#      - 설명
#        - pivot을 정한다. (보통 맨 끝)
#           - loop: smaller 원소를 계속 추적한다.
#             - 현재 원소가 pivot보다 작으면 i++, swap(i,j). (크면 continue)
#           - 루프가 끝나면 swap(smaller+1, pivot)
#           - return piv_idx
