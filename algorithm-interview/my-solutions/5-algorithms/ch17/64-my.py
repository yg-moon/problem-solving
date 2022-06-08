from typing import List
from math import sqrt, pow


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        for p in points:
            dist = sqrt(pow(p[0],2) + pow(p[1],2))
            p.append(dist)
        
        points.sort(key=lambda x: x[2])

        answer = []
        for i in range(k):
            answer.append(points[i][0:2])
        
        return answer
