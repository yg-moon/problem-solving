# 연속합 2
N = int(input())
arr = list(map(int, input().split()))

# dp[0][j]: 그냥 진행한 경우
# dp[1][j]: 원소를 제거한 경우
dp = [[x for x in arr] for _ in range(2)]

for i in range(1, N):
    # 1. 그냥 진행하는 경우
    dp[0][i] = max(dp[0][i], dp[0][i - 1] + arr[i])
    # 2. 원소를 제거하는 경우
    # - max(현재 원소를 제거 vs 이미 제거한 경우)
    dp[1][i] = max(dp[0][i - 1], dp[1][i - 1] + arr[i])

print(max(max(dp[0]), max(dp[1])))

"""
- 난이도: 골드5
- 분류: dp

- 요약: 삭제 여부를 나누어 생각하는 2차원 dp 유형
- 참고: https://ji-gwang.tistory.com/289
"""
