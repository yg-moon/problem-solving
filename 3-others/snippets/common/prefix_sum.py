# 누적합은 전부 1-idx 사용


# 사용법: sum[L, R] = P[R] - P[L-1]
def prefix_sum(arr):
    N = len(arr)
    psum = [0] * (N + 1)

    for i in range(1, N + 1):
        psum[i] = psum[i - 1] + arr[i - 1]

    return psum


# Test
array = [1, 2, 3, 4, 5]
P = prefix_sum(array)
print(array)
print(P)
print(P[4] - P[2 - 1])
print()


# 사용법: sum[(x1, y1) ~ (x2, y2)] =
#   psum[x2][y2] - psum[x1 - 1][y2] - psum[x2][y1 - 1] + psum[x1 - 1][y1 - 1])
#   (전체 구간) - (가로 구간) - (세로 구간) + (겹쳐서 뺀 구간)
def prefix_sum_2d(mat):
    N = len(mat)
    M = len(mat[0])
    psum = [[0] * (M + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1, M + 1):
            # psum[i][j]: (0,0) ~ (i,j) 사각형의 누적합
            psum[i][j] = (
                # (원래 데이터의 값) + (가로 구간) + (세로 구간) - (겹쳐서 더한 구간)
                mat[i - 1][j - 1]
                + psum[i - 1][j]
                + psum[i][j - 1]
                - psum[i - 1][j - 1]
            )

    return psum


# Test
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
P2 = prefix_sum_2d(matrix)

for row in matrix:
    print(row)
print()

for row in P2:
    print(row)
print()

print(P2[2][2] - P2[1 - 1][2] - P2[2][1 - 1] + P2[1 - 1][1 - 1])
