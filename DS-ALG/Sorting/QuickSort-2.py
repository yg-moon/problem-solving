# Lomuto parition scheme
# 요약: 작은 걸 찾아 계속 왼쪽으로 보내다가, 마지막에 pivot을 중간에 놓는 방식
def quickSort(A, lo, hi):
    def partition(lo, hi):
        # pivot은 맨 마지막 원소
        pivot = A[hi]
        i = lo
        for j in range(lo, hi):
            # 현재 원소가 pivot보다 작으면 swap(i, j) & i++
            if A[j] < pivot:
                A[i], A[j] = A[j], A[i]
                i += 1
        # 루프가 끝나면 swap(i, hi)
        A[i], A[hi] = A[hi], A[i]
        # i를 리턴
        return i

    if lo < hi:
        pivot = partition(lo, hi)
        quickSort(A, lo, pivot - 1)
        quickSort(A, pivot + 1, hi)


A = [38, 27, 43, 3, 9, 82, 10]
quickSort(A, 0, len(A) - 1)
print(A)