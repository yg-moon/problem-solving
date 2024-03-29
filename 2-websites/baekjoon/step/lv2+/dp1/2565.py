# 전깃줄
N = int(input())
arr = []
for _ in range(N):
    a, b = map(int, input().split())
    arr.append((a, b))

# 전처리: (a,b)에서 a를 기준으로 정렬한 이후 b만 빼오기
arr = [b for (a, b) in sorted(arr)]

# LIS
# dp[i]: i번째 원소까지 진행했을때 LIS의 길이
dp = [1] * N
for i in range(N):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

# 정답 = 전체 전깃줄 - LIS의 길이
print(N - max(dp))

"""
- 난이도: 골드5
- 분류: dp

- LIS를 떠올리는게 중요했던 문제
"""
