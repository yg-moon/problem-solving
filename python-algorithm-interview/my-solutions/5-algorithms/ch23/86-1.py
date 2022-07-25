from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 값을 누적해서 더하다가, 더하려는 누적값이 0 이하면 버린다
        for i in range(1, len(nums)):
            # 직전 누적값이 0 이상일 때만 더하고, 아니면 원래 값 쓰기.
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
        # nums[i]에 ‘i 까지 진행했을 때 연속서브배열 합의 최대치’가 들어간다.
        return max(nums)
