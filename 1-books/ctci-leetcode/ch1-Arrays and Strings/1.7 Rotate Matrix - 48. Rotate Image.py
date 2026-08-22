from typing import List


class Solution:
    # Sol. 뒤집고 전치
    def rotate(self, mat: List[List[int]]) -> None:
        N = len(mat)

        # 1. 행의 순서를 뒤집음
        mat.reverse()

        # 2. Transpose
        for i in range(N):
            for j in range(i + 1, N):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

    # Bonus. 반시계 방향
    def anti_rotate(mat):
        N = len(mat)

        # 1. 각 행의 내용을 뒤집음
        for i in range(N):
            mat[i].reverse()

        # 2. Transpose
        for i in range(N):
            for j in range(i + 1, N):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]


"""
- 난이도: Medium
- 분류: 수학
"""
