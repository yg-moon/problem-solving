# 퇴사
N = int(input())
T = []
P = []
for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

# dp[i]: i번째 날에 얻을 수 있는 최대 수익
dp = [0] * (N + 1)
max_val = 0

for i in range(N + 1):
    # 현재 날짜는 지금까지의 최댓값으로 채우기
    max_val = max(max_val, dp[i])
    dp[i] = max_val
    # 상담을 완료하는 날이 퇴사일을 넘기지 않는다면
    if i < N and i + T[i] <= N:
        # 해당 날짜에 대해 (그냥 놔두기 vs 상담하기) 중에서 수익이 큰쪽을 선택
        dp[i + T[i]] = max(dp[i + T[i]], dp[i] + P[i])

print(dp[N])

"""
- 난이도: 실버3
- 분류: dp

- 요약: 가능한 경우를 갱신하는 1차원 dp 유형
- 참고: https://codejin.tistory.com/173
"""
