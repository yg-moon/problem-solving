N = int(input())
arr = list(map(int, input().split()))


def binary_search():
    left = 0
    right = N - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] > mid:
            right = mid - 1
        elif arr[mid] < mid:
            left = mid + 1
        else:
            return mid
    return -1


print(binary_search())
