# Lomuto parition scheme (직관적인 버전)
# 요약: 작은걸 찾아서 왼쪽으로 보내는 방식
def partition(A, lo, hi):
    # 피봇은 맨 마지막 원소 (다른걸 선택해도 되지만, 일단 맨끝에 둬야함)
    pivot = A[hi]
    i = lo

    for j in range(lo, hi):
        # 현재 원소가 pivot보다 작으면 swap(i, j) & i++
        if A[j] < pivot:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[i], A[hi] = A[hi], A[i]  # 피봇을 중간에 놓기
    return i  # 피봇의 인덱스 리턴


def quickSort(A, lo, hi):
    if lo < hi:
        pivot = partition(A, lo, hi)
        quickSort(A, lo, pivot - 1)
        quickSort(A, pivot + 1, hi)


A = [38, 27, 43, 3, 9, 82, 10]
quickSort(A, 0, len(A) - 1)
print(A)
