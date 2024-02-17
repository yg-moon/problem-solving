from typing import List


class Solution:
    @staticmethod
    def compare(n1: int, n2: int) -> bool:
        return str(n1) + str(n2) < str(n2) + str(n1)

    def largestNumber(self, nums: List[int]) -> str:
        # Insertion sort
        for i in range(1, len(nums)):
            j = i
            while j > 0 and self.compare(nums[j - 1], nums[j]):
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
                j -= 1
        return str(int("".join(map(str, nums))))
