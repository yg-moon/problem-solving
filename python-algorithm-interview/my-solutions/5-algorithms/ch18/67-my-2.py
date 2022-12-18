from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return [x for x in set(nums1) if x in set(nums2)]
