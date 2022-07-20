def solution(nums):
    num_set = set(nums)
    N_set = len(num_set)
    N_half = len(nums) // 2

    if N_half <= N_set:
        return N_half
    else:
        return N_set
