# 연속합
n = int(input())
arr = list(map(int, input().split()))

# dp[i]: i번째 원소까지 고려했을때 최대 연속합
dp = [0] * n

# 초기화
dp[0] = arr[0]

# 핵심
for i in range(1, n):
    # 현재 누적값 = max(현재 배열값, 이전 누적값 + 현재 배열값)
    dp[i] = max(arr[i], dp[i - 1] + arr[i])

print(max(dp))

"""
- 난이도: 실버2
- 분류: dp

- 가장 기본적인 연속합
"""
