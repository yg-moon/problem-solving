from collections import deque
from typing import List

INF = int(1e9)


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        answer = []
        q = deque()
        cur_max = -INF

        for i, num in enumerate(nums):
            q.append(num)

            # 초기 윈도우가 완성되기 전의 값들
            if i < k - 1:
                continue

            # 새로 추가된 값이 기존 최대값보다 큰 경우 교체
            if cur_max == -INF:
                cur_max = max(q)
            elif num > cur_max:
                cur_max = num

            answer.append(cur_max)

            # 최대값이 윈도우에서 빠지면 초기화
            if q.popleft() == cur_max:
                cur_max = -INF

        return answer


# TLE
