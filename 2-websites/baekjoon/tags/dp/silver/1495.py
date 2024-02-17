# 기타리스트
N, S, M = map(int, input().split())
arr = [0] + list(map(int, input().split()))  # 1-idx
answer = -1

# dp[i][j]: i번째 곡을 j의 볼륨으로 플레이 가능한지 여부
dp = [[False] * (M + 1) for _ in range(N + 1)]
# 초기화
if S - arr[1] >= 0:
    dp[1][S - arr[1]] = True
if S + arr[1] <= M:
    dp[1][S + arr[1]] = True

for i in range(2, N + 1):
    for j in range(M + 1):
        # 핵심: 이전 곡의 연주 가능한 볼륨에 대해
        if dp[i - 1][j] == True:
            # 볼륨을 내리는 경우
            if j - arr[i] >= 0:
                dp[i][j - arr[i]] = True
            # 볼륨을 올리는 경우
            if j + arr[i] <= M:
                dp[i][j + arr[i]] = True

# 마지막 노래의 최대 볼륨을 찾기
for j in range(M, -1, -1):
    if dp[N][j] == True:
        answer = j
        break

print(answer)

"""
- 난이도: 실버1
- 분류: dp

- 요약: dp 배열의 정의가 특이한 유형
"""
