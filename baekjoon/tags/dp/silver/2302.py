# 극장 좌석
N = int(input())
M = int(input())
vips = [int(input()) for _ in range(M)]

# dp[i]: 빈 좌석이 i개일때 앉을 수 있는 경우의 수
dp = [0] * 41
# 초기화
dp[0] = 1
dp[1] = 1
dp[2] = 2

# 핵심1: 피보나치임을 파악하기
for i in range(3, N + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

# 핵심2: vip석 기준으로 끊어서 곱하기
answer = 1
start = 1

for vip in vips:
    end = vip
    answer *= dp[end - start]
    start = end + 1

answer *= dp[N - start + 1]

print(answer)

"""
- 난이도: 실버1
- 분류: dp

- 요약: dp값이 직접 정답이 아닌 유형 + 피보나치
- 참고: https://yabmoons.tistory.com/550
"""
