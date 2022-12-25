def solution(nums):
    set_nums = set(nums)
    len_set = len(set_nums)
    len_half = len(nums) // 2

    if len_set <= len_half:
        return len_set
    else:
        return len_half


"""
- '전체 길이 절반'과 'set의 길이'를 비교해서, 더 작은 쪽을 리턴.
"""
