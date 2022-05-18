import bisect
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, num in enumerate(numbers):
            diff = target - num
            j = bisect.bisect_left(numbers, diff)
            if i != j and j < len(numbers) and numbers[j] == diff: 
                return sorted([i + 1, j + 1])
        return -1
