# 정석 버전
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

    while i < len(L) and j < len(R):
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
