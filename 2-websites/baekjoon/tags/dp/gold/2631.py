# 줄세우기
N = int(input())
arr = [int(input()) for _ in range(N)]

# dp[i]: i번째 글자까지 고려한 LIS의 길이
dp = [1] * N

# LIS
for i in range(N):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

# 답: N - LIS의 길이
print(N - max(dp))

"""
- 난이도: 골드4
- 분류: dp

- 요약: LIS 유형

해설
- LIS 유형인걸 파악하는게 중요했던 문제
- 힌트: 목표는 옮겨야 되는 최소 횟수를 찾는 것
- 핵심: 반대로 생각해서, 옮기지 않아도 되는 (이미 규칙을 지키고 있는) 최대 길이를 구해서, 전체에서 빼면 됨
"""
