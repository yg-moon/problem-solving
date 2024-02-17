import sys
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = sys.maxsize

        # Keep updating both variables
        for i in range(len(prices)):
            min_price = min(min_price, prices[i])
            max_profit = max(max_profit, prices[i] - min_price)

        return max_profit


### Time Complexity
# O(n)

### Note
# 브루트 포스로 O(n^2)인 문제를 단순한 아이디어를 통해 O(n)으로 줄인게 중요한 문제.
