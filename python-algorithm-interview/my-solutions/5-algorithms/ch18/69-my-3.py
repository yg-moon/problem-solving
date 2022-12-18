from typing import List
import bisect


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 열의 개수 줄이기
        row_len = len(matrix[0])
        hi = row_len
        # 행의 개수 줄이기
        first_col = [row[0] for row in matrix]
        row_num = bisect.bisect_left(first_col, target)

        for i in range(row_num + 1):
            if i < len(matrix):
                if matrix[i][0] > target:
                    break
                j = bisect.bisect_left(matrix[i], target, 0, hi)
                if j < len(matrix[0]) and matrix[i][j] == target:
                    return True
                if j < hi:
                    hi = j
        return False
