from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 투포인터 풀이
        left, right = 0, len(numbers) - 1
        while not left == right:
            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                return left + 1, right + 1
