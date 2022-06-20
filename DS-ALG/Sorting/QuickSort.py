# Hoare parition scheme
# 요약: 왼쪽에서 pivot보다 큰 걸 찾고, 오른쪽에서 pivot보다 작은걸 찾아 계속 swap
def partition(A, lo, hi):
    # pivot은 맨 처음 원소
    piv_idx = lo
    pivot = A[lo]
    
    while lo < hi:
        while lo < len(A) and A[lo] <= pivot:
            lo += 1
        while A[hi] > pivot:
            hi -= 1
        if lo < hi:
            A[lo], A[hi] = A[hi], A[lo]
    
    # lo > hi 가 될 때, swap(hi, piv_idx) 하면 끝
    A[hi], A[piv_idx] = A[piv_idx], A[hi]
    # hi를 리턴
    return hi


def quick_sort(A, lo, hi):
    if lo < hi:
        p = partition(A, lo, hi)
        quick_sort(A, lo, p-1)
        quick_sort(A, p+1, hi)


array = [10, 7, 8, 9, 1, 5]
quick_sort(array, 0, len(array) - 1)
print(f"Sorted array: {array}")