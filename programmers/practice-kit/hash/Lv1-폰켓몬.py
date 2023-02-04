def solution(nums):
    len_half = len(nums) // 2
    len_set = len(set(nums))

    # '전체 길이 절반'과 'set의 길이'를 비교해서, 더 작은 쪽을 리턴
    return min(len_half, len_set)
