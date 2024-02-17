# BOJ 18353
# 출처: 이코테
N = int(input())
arr = list(map(int, input().split()))
arr.reverse()

# LIS
dp = [1] * N
for i in range(1, N):
    for j in range(0, i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

# 열외해야 하는 병사의 최소 수
print(N - max(dp))
