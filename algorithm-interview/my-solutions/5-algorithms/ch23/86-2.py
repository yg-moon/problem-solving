import sys
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best_sum = -sys.maxsize
        current_sum = 0
        # 카데인: 배열을 한번만 훑으면서, 매 상태에서 현재까지의 정보를 업데이트하는 방식.
        for num in nums:
            # current_sum에서 결국 값을 누적할지, 자신으로 초기화할지 결정하므로 로직은 풀이1과 동일.
            current_sum = max(num, current_sum + num)
            best_sum = max(best_sum, current_sum)

        return best_sum
