from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []

        def dfs(elements, idx):
            results.append(elements[:])

            for i in range(idx, len(nums)):
                elements.append(nums[i])
                dfs(elements, i + 1)
                elements.pop()

        dfs([], 0)
        return results
