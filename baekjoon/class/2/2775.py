# 부녀회장이 될테야
T = int(input())

for _ in range(T):
    K = int(input())
    N = int(input())

    # dp[i][j]: i층 j호에 사는 사람수 (0층 1호부터 시작)
    dp = [[0] * (N + 1) for _ in range(K + 1)]

    # "0층의 i호에는 i명이 산다"
    for i in range(1, N + 1):
        dp[0][i] = i

    # "a층의 b호에 살려면 자신의 아래층의 1호부터 b호까지 사람들의 수의 합만큼 사람들을 데려와 살아야 한다"
    for a in range(1, K + 1):
        for b in range(1, N + 1):
            for c in range(1, b + 1):  # 주의: range(0) 이면 아예 작동하지 않음
                dp[a][b] += dp[a - 1][c]

    # k층 n호에 사는 사람수
    print(dp[K][N])

"""
- 난이도: 브론즈1
- 분류: dp
"""
