# 별 찍기 - 11
# 출처: https://ku-hug.tistory.com/149
N = int(input())
answer = [[" "] * 2 * N for _ in range(N)]


def solve(i, j, n):
    # n == 3 이면 삼각형을 그림
    # (i,j)는 현재 꼭짓점의 좌표
    if n == 3:
        answer[i][j] = "*"
        answer[i + 1][j - 1] = answer[i + 1][j + 1] = "*"
        for k in range(-2, 3):
            answer[i + 2][j - k] = "*"
    # 아닐 경우, 절반 크기의 삼각형 3개로 분할하여 재귀호출
    else:
        half = n // 2
        solve(i, j, half)
        solve(i + half, j - half, half)
        solve(i + half, j + half, half)


solve(0, N - 1, N)

for row in answer:
    print("".join(row))

"""
- 난이도: 골드4
- 분류: 분할정복

핵심
- 전체 배열 크기는 N x 2N 이다.
- 분할정복은 절반 크기의 삼각형 3개를 재귀호출하면 된다.
    - 재귀는 꼭대기 별에서 시작해서, 현재 크기의 절반만큼 떨어진 나머지 두 꼭대기에서 시작하면 된다.
- 실제 출력은 n=3 일때, 현재 꼭짓점 좌표 (i,j)를 기준으로 기본 삼각형을 그리면 된다.
"""
