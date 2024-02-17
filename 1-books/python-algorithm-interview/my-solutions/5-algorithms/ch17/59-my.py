from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        answer = []
        start = intervals[0][0]
        end = intervals[0][1]

        for intv in intervals:
            if end >= intv[0]:
                end = max(end, intv[1])
            else:
                answer.append([start, end])
                start = intv[0]
                end = intv[1]

        answer.append([start, end])  # 맨 마지막 범위
        return answer
