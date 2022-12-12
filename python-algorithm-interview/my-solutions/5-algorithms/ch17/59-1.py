from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        answer = []
        for intv in intervals:
            if answer and answer[-1][1] >= intv[0]:
                answer[-1][1] = max(answer[-1][1], intv[1])
            else:
                answer += [intv]
        return answer
