from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deq = deque()
        answer = []

        for i in range(len(nums)):
            # 데크의 맨앞에 윈도우를 벗어난 인덱스가 있다면 제거
            if deq and i - deq[0] == k:
                deq.popleft()
            # 데크의 뒤에서부터 현재 추가할 숫자보다 작으면 제거 (데크에 불필요한 숫자가 없도록)
            while deq and nums[deq[-1]] <= nums[i]:
                deq.pop()
            # 데크에 현재 숫자의 인덱스 추가 (인덱스만 저장하여 공간 아낌)
            deq.append(i)
            # 현재 윈도우 크기가 k보다 클 때, 데크의 맨앞에 있는 수(현재 윈도우의 max)를 정답에 추가
            if i + 1 >= k:
                answer.append(nums[deq[0]])

        return answer
