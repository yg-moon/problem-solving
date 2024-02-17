# 동전 2
N, K = map(int, input().split())
coins = set([int(input()) for _ in range(N)])

MAX = 10001  # 주의: 더 작게 잡으면 틀림!

# dp[i]: i원을 만들기 위해 필요한 동전의 최소 개수
dp = [MAX] * (K + 1)

# 초기화
dp[0] = 0

# 점화식
for c in coins:  # 각 동전에 대해
    for i in range(c, K + 1):  # 동전 이상의 금액부터 시작해서 끝까지
        dp[i] = min(dp[i], dp[i - c] + 1)  # 동전을 뺀 금액에서 +1 하는게 더 적은 횟수인지 확인

if dp[K] == MAX:
    print(-1)
else:
    print(dp[K])

"""
- 난이도: 골드5
- 분류: dp
- 소요 시간: 15분

- 요약: 가능한 모든 경우를 갱신하는 1차원 dp 유형

디버깅: 틀렸습니다
- 원인: MAX를 너무 작은 값으로 잡았음 (101이 아니라 최소 10001로 잡았어야 함) 
"""
