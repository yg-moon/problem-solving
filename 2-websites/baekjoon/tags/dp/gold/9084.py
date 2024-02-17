# 동전
T = int(input())

for _ in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    M = int(input())

    # dp[i]: i원을 만드는 방법의 개수
    dp = [0] * (M + 1)

    # 초기화
    dp[0] = 1  # 주의: 이걸 틀려서 못 풀었음

    # 점화식
    for c in coins:  # 각 동전에 대해
        for i in range(c, M + 1):  # 동전 이상의 금액부터 시작해서 끝까지
            dp[i] += dp[i - c]  # 이전에서 가능한 모든 가짓수를 더해줌

    print(dp[M])

"""
- 난이도: 골드5
- 분류: dp

- 요약: 가능한 모든 경우를 갱신하는 1차원 dp

동전 문제 공통점
- 초기화: 0의 경우만 정확하게 해주고, 각 동전에 대해서는 해줄 필요가 없음
- 점화식: 각 동전에 대해 for, 동전 이상 금액에 대해 for
"""
