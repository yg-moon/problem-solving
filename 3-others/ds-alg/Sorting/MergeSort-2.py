def mergeSort(A, l, r):
    if l < r:
        mid = l + (r - l) // 2
        mergeSort(A, l, mid)
        mergeSort(A, mid + 1, r)
        merge(A, l, mid, r)


def merge(A, l, m, r):
    # L, R 채우기
    L = []
    R = []
    for i in range(l, m + 1):
        L.append(A[i])
    for i in range(m + 1, r + 1):
        R.append(A[i])

    # 값 비교해가며 merge
    i = 0
    j = 0
    k = l

    while i < len(L) and j < len(R):  # 주의: 포함 여부 조심!
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1

    # 남아 있으면 털어넣기
    while i < len(L):
        A[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        A[k] = R[j]
        j += 1
        k += 1


def printlist(A):
    for i in range(len(A)):
        print(A[i], end=" ")
    print()


if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array: ")
    printlist(arr)
    mergeSort(arr, 0, len(arr) - 1)
    print("Sorted array: ")
    printlist(arr)


# - Python:
#   - Error: list assignment index out of range: list에 append로 안 붙여서 그렇다.
#   - 배열처럼 쓰려면 미리 초기화 해야 함:  L = [0] * n1
#
# - 구현
#   - 의미가 있거나, 자주 쓰는건 변수로 설정.
#   - 오버플로우 방지를 위해 mid = start + (end - start) // 2 로 구한다. (오버플로우 방지)
#
# - 디버깅
#   - 멍청했다. R[j] 이어야 하는 부분을 코드 고치다가 L[j] 로 써놨다.
