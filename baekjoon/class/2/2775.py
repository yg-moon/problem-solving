# 부녀회장이 될테야
T = int(input())

for _ in range(T):
    K = int(input())
    N = int(input())

    dp = [[0] * N for _ in range(K + 1)]  # 주의: K는 0층부터 시작하므로, (K + 1)로 생성

    # 0층 채우기
    for j in range(N):
        dp[0][j] = j + 1

    # "a층의 b호에 살려면 자신의 아래층의 1호부터 b호까지 사람들의 수의 합만큼 사람들을 데려와 살아야 한다"
    for i in range(1, K + 1):
        for j in range(N):
            for k in range(j + 1):  # 주의: range(0) 이면 아예 작동하지 않음
                dp[i][j] += dp[i - 1][k]

    # k층 n호에 사는 사람수
    print(dp[K][N - 1])

"""
- 난이도: 브론즈1
- 분류: dp
"""
