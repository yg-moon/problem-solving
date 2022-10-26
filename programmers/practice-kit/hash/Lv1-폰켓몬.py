def solution(nums):
    set_nums = set(nums)
    len_set = len(set_nums)
    len_half = len(nums) // 2

    if len_half <= len_set:
        return len_half
    else:
        return len_set
