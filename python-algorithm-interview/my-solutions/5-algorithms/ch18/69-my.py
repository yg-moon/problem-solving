import bisect
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 열의 개수 줄이기
        row_len = len(matrix[0])
        hi = row_len
        for row in matrix:
            if row[0] > target:
                break
            i = bisect.bisect_left(row, target, 0, hi)
            if i < row_len and row[i] == target:
                return True
            if i < hi:
                hi = i
        return False
