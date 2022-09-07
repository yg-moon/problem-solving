# BOJ 1932
N = int(input())
dp = []
for _ in range(N):
    dp.append(list(map(int, input().split())))

for i in range(1, N):
    for j in range(i + 1):
        # 맨 왼쪽 숫자인 경우: 위쪽 값만 더한다.
        if j == 0:
            dp[i][j] += dp[i - 1][j]
        # 맨 오른쪽 숫자인 경우: 왼쪽 위 값만 더한다.
        elif j == i:
            dp[i][j] += dp[i - 1][j - 1]
        # 나머지: max(위쪽, 왼쪽 위) 값을 더한다.
        else:
            dp[i][j] += max(dp[i - 1][j], dp[i - 1][j - 1])

# 마지막 행의 최댓값
answer = max(dp[N - 1])
print(answer)
