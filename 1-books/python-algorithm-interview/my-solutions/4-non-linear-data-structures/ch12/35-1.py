# LeetCode 77
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def dfs(elements, start, k):
            # k가 0이면 현재 조합을 정답에 추가
            if k == 0:
                result.append(elements[:])
                return

            # 자신 이후의 값만 고려하기: start + 1
            # 남은 개수 계산하기: k - 1
            for i in range(start, n + 1):
                elements.append(i)
                dfs(elements, i + 1, k - 1)
                elements.pop()

        dfs([], 1, k)
        return result
