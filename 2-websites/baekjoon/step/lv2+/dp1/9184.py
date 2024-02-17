# 신나는 함수 실행

# 핵심1: 범위는 0~20만 고려하면 됨
# (0보다 작으면 1을 리턴하고, 20보다 크면 w(20,20,20)으로 통일하기 때문)
dp = [[[0] * 21 for _ in range(21)] for _ in range(21)]


def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    # 핵심2: 이미 계산한 적이 있으면, 그대로 리턴
    if dp[a][b][c]:
        return dp[a][b][c]
    # 핵심3: 아직 계산한 적이 없으면, dp 배열에 값을 기록하고 리턴
    if a < b < c:
        dp[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
        return dp[a][b][c]
    else:
        dp[a][b][c] = (
            w(a - 1, b, c)
            + w(a - 1, b - 1, c)
            + w(a - 1, b, c - 1)
            - w(a - 1, b - 1, c - 1)
        )
        return dp[a][b][c]


while True:
    a, b, c = map(int, input().split())
    if (a, b, c) == (-1, -1, -1):
        break
    print(f"w({a}, {b}, {c}) = {w(a, b, c)}")

"""
- 난이도: 실버2
- 분류: dp

- 요약: Top-Down DP의 기본을 배우는 예제
- 출처: https://jainn.tistory.com/82
"""
