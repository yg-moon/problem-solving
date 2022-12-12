from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        answer = []
        i = 0

        while i < len(intervals):
            start = intervals[i][0]
            end = intervals[i][1]
            while True:
                if i < len(intervals) - 1 and end >= intervals[i + 1][0]:
                    end = max(end, intervals[i + 1][1])
                    i += 1
                else:
                    break
            answer.append([start, end])
            i += 1

        return answer
