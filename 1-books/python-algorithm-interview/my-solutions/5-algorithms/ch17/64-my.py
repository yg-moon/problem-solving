from typing import List
from math import sqrt


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        for point in points:
            x, y = point
            dist = sqrt((x**2) + (y**2))
            point.append(dist)

        points.sort(key=lambda x: x[2])

        return [p[:2] for p in points[0:k]]
        # Equivalent to:
        # answer = []
        # for i in range(k):
        #     answer.append(points[i][:2])
        # return answer
