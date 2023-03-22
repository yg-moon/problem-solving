# 별 찍기 - 10
N = int(input())
answer = [[" "] * N for _ in range(N)]


def solve(i, j, n):
    # n == 3 이면 기본패턴을 출력
    # (i,j)는 현재 좌상단의 좌표
    if n == 3:
        for x in range(i, i + 3):
            for y in range(j, j + 3):
                answer[x][y] = "*"
        answer[i + 1][j + 1] = " "
    # 아닐 경우, 1/3 크기의 패턴 8개로 분할하여 재귀호출
    else:
        third = n // 3
        for x in range(3):
            for y in range(3):
                if not (x == 1 and y == 1):
                    solve(i + third * x, j + third * y, third)


solve(0, 0, N)

for row in answer:
    print("".join(row))

"""
- 난이도: 골드5
- 분류: 분할정복

- BOJ #2448 '별 찍기 - 11'에서 배운 풀이를 적용했다.
"""
