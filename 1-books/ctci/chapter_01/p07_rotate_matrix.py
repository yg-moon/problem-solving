# O(NxN)
import unittest
from copy import deepcopy


def rotate_matrix(matrix):
    """rotates a matrix 90 degrees clockwise"""
    n = len(matrix)
    for layer in range(n // 2):
        first = layer
        last = n - layer - 1
        for i in range(first, last):
            # get offset
            offset = i - first

            # save top
            top = matrix[first][i]

            # 1. left -> top
            matrix[first][i] = matrix[last - offset][first]

            # 2. bottom -> left
            matrix[last - offset][first] = matrix[last][last - offset]

            # 3. right -> bottom
            matrix[last][last - offset] = matrix[i][last]

            # 4. top -> right
            matrix[i][last] = top
    return matrix


def rotate_matrix_double_swap(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

    for i in range(n):
        for j in range(int(n / 2)):
            temp = matrix[i][j]
            matrix[i][j] = matrix[i][n - 1 - j]
            matrix[i][n - 1 - j] = temp
    return matrix


def rotate_matrix_pythonic(matrix):
    """rotates a matrix 90 degrees clockwise"""
    n = len(matrix)
    result = [[0] * n for i in range(n)]  # empty list of 0s
    for i, j in zip(range(n), range(n - 1, -1, -1)):  # i counts up, j counts down
        for k in range(n):
            result[k][i] = matrix[j][k]
    return result


def rotate_matrix_pythonic_alternate(matrix):
    """rotates a matrix 90 degrees clockwise"""
    return [list(reversed(row)) for row in zip(*matrix)]


def my_sol(mat):
    N = len(mat)
    ret = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            ret[j][N - i - 1] = mat[i][j]
    return ret


def my_sol_2(mat):
    return list(map(list, zip(*mat[::-1])))


class Test(unittest.TestCase):
    test_cases = [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[7, 4, 1], [8, 5, 2], [9, 6, 3]]),
        (
            [
                [1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 17, 18, 19, 20],
                [21, 22, 23, 24, 25],
            ],
            [
                [21, 16, 11, 6, 1],
                [22, 17, 12, 7, 2],
                [23, 18, 13, 8, 3],
                [24, 19, 14, 9, 4],
                [25, 20, 15, 10, 5],
            ],
        ),
    ]
    testable_functions = [
        rotate_matrix_pythonic,
        rotate_matrix,
        rotate_matrix_pythonic_alternate,
        rotate_matrix_double_swap,
        my_sol,
        my_sol_2,
    ]

    def test_rotate_matrix(self):
        for f in self.testable_functions:
            for [test_matrix, expected] in self.test_cases:
                test_matrix = deepcopy(test_matrix)
                assert f(test_matrix) == expected


if __name__ == "__main__":
    unittest.main()
