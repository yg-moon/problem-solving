# 전깃줄
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 전처리: (a,b)에서 a를 기준으로 정렬한 이후 b만 빼오기
arr = [x for [_, x] in sorted(arr)]

# dp[i]: i번째 원소까지 진행했을때 LIS의 길이
# 주의: 1로 초기화
dp = [1] * N

# LIS
for i in range(N):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

# 정답: 전체 전깃줄 개수 - LIS의 길이
print(N - max(dp))

"""
- 난이도: 골드5
- 분류: dp

- 핵심: '정답: 전체 - LIS' 라는 발상
"""
