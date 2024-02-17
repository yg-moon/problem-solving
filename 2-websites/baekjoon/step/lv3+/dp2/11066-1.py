# 파일 합치기
# 출처: https://js1jj2sk3.tistory.com/3
T = int(input())

for _ in range(T):
    K = int(input())
    files = [0] + list(map(int, input().split()))  # 누적합을 위해 1-idx
    psum = [0] * (K + 1)

    # dp[i][j]: 구간 [i,j]을 합치는 최소비용
    dp = [[0] * (K + 1) for _ in range(K + 1)]

    # 누적합 계산
    for i in range(1, K + 1):
        psum[i] = psum[i - 1] + files[i]

    # 핵심: dp[i][j] = min(i<=k<j){dp[i][k] + dp[k+1][j]} + psum[i][j]
    for gap in range(1, K + 1):
        for i in range(1, K + 1 - gap):
            j = i + gap
            dp[i][j] = int(1e9)
            for k in range(i, j):
                dp[i][j] = min(
                    dp[i][j],
                    dp[i][k] + dp[k + 1][j] + psum[j] - psum[i - 1],
                )

    print(dp[1][K])

"""
- 난이도: 골드3
- 분류: dp

- 유형: 구간 쪼개기 dp + 누적합
"""
