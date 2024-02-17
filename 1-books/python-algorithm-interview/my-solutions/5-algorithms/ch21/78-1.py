from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        # 단순하게, 다음날 값이 오르는 경우에는 무조건 거래. 
        for i in range(len(prices) - 1):
            if prices[i + 1] > prices[i]:
                result += prices[i + 1] - prices[i]
        return result
