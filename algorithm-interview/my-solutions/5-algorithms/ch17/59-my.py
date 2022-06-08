from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals

        intervals.sort()
        range_start = intervals[0][0]
        range_end = intervals[0][1]
        answer = []

        for interval in intervals:
            if range_start <= interval[0] <= range_end:
                range_end = max(range_end, interval[1])
            else:
                answer.append([range_start, range_end])
                range_start = interval[0]
                range_end = interval[1]
        answer.append([range_start, range_end])

        return answer
