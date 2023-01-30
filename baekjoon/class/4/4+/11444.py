# 피보나치 수6
# 출처: https://star7sss.tistory.com/358
n = int(input())
matrix = [[1, 1], [1, 0]]

# 행렬의 곱셈
def mul_mat(mat1, mat2):
    res = [[0] * 2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                # c11 = (a11 * b11) + (a12 * b21)
                res[i][j] += (mat1[i][k] * mat2[k][j]) % 1000000007
    return res


# 행렬의 거듭제곱 (by 분할정복)
def pow_mat(mat, p):
    if p == 1:  # p가 1이 될 때까지 재귀
        return mat
    else:
        tmp_mat = pow_mat(mat, p // 2)  # mat^(p // 2)
        if p % 2 == 0:
            return mul_mat(tmp_mat, tmp_mat)  # p가 짝수인 경우
        else:
            return mul_mat(mul_mat(tmp_mat, tmp_mat), mat)  # p가 홀수인 경우


# n번째 피보나치 수는 행렬 [[1,1],[1,0]]^n 의 1행 2열 값
result = pow_mat(matrix, n)
print(result[0][1] % 1000000007)

"""
- 난이도: 골드2
- 분류: 수학 (분할정복을 이용한 거듭제곱)

요약
- 아주 큰 수의 피보나치를 구하기 위해서는 행렬의 거듭제곱을 이용해야 한다.
- n번째 피보나치 수는 행렬 [[1,1],[1,0]]^n 의 1행 2열 값이다.
"""
