from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        answer = []
        for intv in sorted(intervals, key=lambda x: x[0]):
            if answer and intv[0] <= answer[-1][1]:
                answer[-1][1] = max(answer[-1][1], intv[1])
            else:
                answer += [intv]
        return answer
