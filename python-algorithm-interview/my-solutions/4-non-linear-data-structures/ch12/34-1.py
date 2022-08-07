# LeetCode 46
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        temp = []

        def dfs(elements):
            # 리프노드이면 결과에 추가
            if len(elements) == 0:
                result.append(temp[:])
                return
            # 순열 생성
            for e in elements:
                other_elements = elements[:]
                other_elements.remove(e)
                # 핵심: append -> dfs -> pop
                temp.append(e)
                dfs(other_elements)
                temp.pop()

        dfs(nums)
        return result
