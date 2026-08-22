from typing import List


class Solution:
    # 방법1. 모든 0의 좌표를 저장
    # O(MN) space
    def setZeroes(self, matrix: List[List[int]]) -> None:
        M = len(matrix)
        N = len(matrix[0])

        zeros = []

        for i in range(M):
            for j in range(N):
                if matrix[i][j] == 0:
                    zeros.append((i, j))

        for x, y in zeros:
            for i in range(M):
                matrix[i][y] = 0
            for j in range(N):
                matrix[x][j] = 0

    # 방법2. 0이 될 행과 열을 저장
    # O(M+N) space
    def setZeroes(self, matrix: List[List[int]]) -> None:
        M = len(matrix)
        N = len(matrix[0])

        rows = set()
        cols = set()

        for i in range(M):
            for j in range(N):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        for i in rows:
            for j in range(N):
                matrix[i][j] = 0

        for j in cols:
            for i in range(M):
                matrix[i][j] = 0

    # Sol. 첫 행과 열을 마커로 사용
    # O(1) space
    def setZeroes(self, matrix: List[List[int]]) -> None:
        M = len(matrix)
        N = len(matrix[0])
        first_row_has_zero = any(matrix[0][j] == 0 for j in range(N))
        first_col_has_zero = any(matrix[i][0] == 0 for i in range(M))

        # Use first row and column as markers
        for i in range(1, M):
            for j in range(1, N):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        # Zero out cells based on markers
        for i in range(1, M):
            for j in range(1, N):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

        # Zero out the first row if needed
        if first_row_has_zero:
            for j in range(N):
                matrix[0][j] = 0

        # Zero out the first column if needed
        if first_col_has_zero:
            for i in range(M):
                matrix[i][0] = 0


"""
- 난이도: Medium
- 분류: 구현
"""
