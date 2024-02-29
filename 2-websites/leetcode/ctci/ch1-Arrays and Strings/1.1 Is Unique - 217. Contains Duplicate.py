from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == len(set(nums)):
            return False
        return True


"""
- 난이도: Easy
- 분류: 해시, 정렬
"""
