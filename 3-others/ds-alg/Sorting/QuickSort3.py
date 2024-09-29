# Hoare parition scheme (효율적인 버전)
# 요약: 왼쪽에서 피봇보다 큰 걸 찾고, 오른쪽에서 피봇보다 작은걸 찾아 계속 스왑
def partition(A, lo, hi):
    # 피봇은 맨 처음 원소 (다른걸 골라도 되지만, 일단 맨앞에 둬야함)
    pivot = A[lo]
    piv_idx = lo

    while lo < hi:
        while lo < len(A) and A[lo] <= pivot:
            lo += 1
        while A[hi] > pivot:
            hi -= 1
        if lo < hi:
            A[lo], A[hi] = A[hi], A[lo]

    A[piv_idx], A[hi] = A[hi], A[piv_idx]  # 피봇을 중간에 놓기
    return hi  # 피봇의 위치를 리턴


def quickSort(A, lo, hi):
    if lo < hi:
        pivot = partition(A, lo, hi)
        quickSort(A, lo, pivot - 1)
        quickSort(A, pivot + 1, hi)


A = [38, 27, 43, 3, 9, 82, 10]
quickSort(A, 0, len(A) - 1)
print(A)
