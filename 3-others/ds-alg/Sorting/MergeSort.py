# 간단 버전
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    def merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result += left[i:]
        result += right[j:]
        return result

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

# 테스트
arr = [3, 6, 8, 10, 1, 2, 1]
print(merge_sort(arr))
