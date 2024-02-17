# 행렬 제곱
# 출처: https://hooongs.tistory.com/114
N, B = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]


def mul_mat(mat1, mat2):
    ret = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                ret[i][j] += (mat1[i][k] * mat2[k][j]) % 1000
    return ret


def pow_mat(mat, b):
    if b == 1:
        return mat
    else:
        root = pow_mat(mat, b // 2)
        if b % 2 == 0:
            return mul_mat(root, root)
        else:
            return mul_mat(mul_mat(root, root), mat)


result = pow_mat(matrix, B)
for row in result:
    for num in row:
        print(num % 1000, end=" ")
    print()

"""
- 난이도: 골드4
- 분류: 수학 (분할정복을 이용한 거듭제곱)

- 비슷한 문제: 'BOJ #11444 - 피보나치 수 6' (거의 동일한 풀이)
"""
