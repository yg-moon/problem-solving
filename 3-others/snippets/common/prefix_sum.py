def prefix_sum(nums):
    n = len(nums)
    psum = [0] * (n + 1)

    for i in range(1, n + 1):
        psum[i] = psum[i - 1] + nums[i - 1]

    return psum


# Example usage
nums = [1, 2, 3, 4, 5]
result = prefix_sum(nums)
print(result)  # Output: [0, 1, 3, 6, 10, 15]
