# 퇴사 2
import sys

# 빠른 입출력
input = sys.stdin.readline

# 팁: 배열을 분리해서 받기
N = int(input())
T = []
P = []
for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

# dp[i]: i번째 날에 얻을 수 있는 최대 수익
dp = [0] * (N + 1)

for i in range(N + 1):
    # 현재 날짜의 최대 수익: 여태까지의 최댓값
    if i > 0:
        dp[i] = max(dp[i], dp[i - 1])
    # 상담을 완료하는 날이 퇴사일을 넘기지 않는다면
    if i < N and i + T[i] <= N:
        # 완료 날짜의 최대 수익: (그냥 놔두기 vs 상담하기) 중에서 수익이 큰 쪽
        dp[i + T[i]] = max(dp[i + T[i]], dp[i] + P[i])

print(dp[N])

"""
- 난이도: 골드5
- 분류: dp

- 요약: 가능한 경우를 갱신하는 1차원 dp 유형
    - N이 15에서 150만으로 늘어서 반드시 dp로 풀어야 하는 문제
    - 즉, 원래 dp 풀이의 난이도는 골드5

- 팁: 풀이를 시각화 해보자. 제대로 이해했는지 알 수 있다.
"""
