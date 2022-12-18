from typing import List
import bisect


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 행의 개수 줄이기
        first_col = [row[0] for row in matrix]
        row_num = bisect.bisect_left(first_col, target)

        for i in reversed(range(row_num + 1)):
            if i < len(matrix):
                j = bisect.bisect_left(matrix[i], target)
                if j < len(matrix[0]) and matrix[i][j] == target:
                    return True
        return False
