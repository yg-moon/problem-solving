from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # i: Red, j: White, k: Blue
        i, j, k = 0, 0, len(nums)

        while j < k:
            if nums[j] < 1:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
                i += 1
            elif nums[j] > 1:
                k -= 1
                nums[j], nums[k] = nums[k], nums[j]
            else:
                j += 1
