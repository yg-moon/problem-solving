from typing import List
import bisect


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, n in enumerate(numbers):
            idx = bisect.bisect_left(numbers, target - n)
            if idx < len(numbers) and i != idx and numbers[idx] == target - n:
                return sorted([i + 1, idx + 1])
