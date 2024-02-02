N = int(input())
arr = list(map(int, input().split()))

# dp[i][j]: i번째 숫자까지 계산했을때 값이 j가 되는 경우의 수
dp = [[0 for _ in range(21)] for _ in range(N)]

# 초기화
dp[0][arr[0]] = 1

# 점화식
for i in range(1, N - 1):
    for j in range(21):
        # 지난 계산기록이 있는 경우에만 진행
        if dp[i - 1][j] != 0:
            if 0 <= j + arr[i] <= 20:
                dp[i][j + arr[i]] += dp[i - 1][j]
            if 0 <= j - arr[i] <= 20:
                dp[i][j - arr[i]] += dp[i - 1][j]

print(dp[N - 2][arr[-1]])

"""
- 정해: dp 배열의 정의가 특이한 유형 (참고: #1495 기타리스트)
    - 힌트: 값이 0~20 사이이므로 dp배열의 기준으로 충분히 고려할만한 작은 크기
    - 로직은 해시맵 버전과 사실상 동일
"""
