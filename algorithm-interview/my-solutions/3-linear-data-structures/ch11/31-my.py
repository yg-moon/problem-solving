from typing import List
from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_count = defaultdict(int)
        answer = []

        # Count frequency for each number
        for num in nums:
            num_to_count[num] += 1

        # Sort dict by values
        sorted_list = sorted(num_to_count.items(), key=lambda item: item[1], reverse=True)

        # Append upto top kth keys
        for i in range(k):
            answer.append(sorted_list[i][0])

        return answer
