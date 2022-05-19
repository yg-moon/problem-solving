from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deq, ans = deque(), []

        for i in range(len(nums)):
            # 데크의 앞에서부터 out of window -> 제거
            if deq and i - deq[0] == k:
                deq.popleft()

            # 데크의 뒤에서부터 현재 추가할 숫자보다 작으면 -> 제거 (deq에 불필요한 숫자 없도록!)
            while deq and nums[deq[-1]] <= nums[i]:
                deq.pop()

            deq.append(i)  # 현재 숫자 추가( (i, num[i])로 저장해도 되나, 인덱스만 저장하여 space 줄임)

            # 출력 (현재 위치 >= window size일 때)
            if i + 1 >= k:
                ans.append(nums[deq[0]])  # 맨 앞은 현재 window 에서 가장 큰 수

        return ans
