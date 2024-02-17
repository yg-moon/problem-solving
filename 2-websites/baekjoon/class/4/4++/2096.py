# 내려가기
# 출처: https://kyun2da.github.io/2021/04/27/goDown/
import sys

input = sys.stdin.readline

N = int(input())

# 핵심: 각 열마다 오직 하나의 변수로 값을 기억하며 진행
max_dp = [0] * 3
min_dp = [0] * 3
max_tmp = [0] * 3
min_tmp = [0] * 3

for _ in range(N):
    # 핵심: 매번 입력을 받으면 즉시 계산
    a, b, c = map(int, input().split())

    # dp 로직은 'BOJ #1149 - RGB 거리' 문제와 유사
    max_tmp[0] = a + max(max_dp[0], max_dp[1])
    max_tmp[1] = b + max(max_dp[0], max_dp[1], max_dp[2])
    max_tmp[2] = c + max(max_dp[1], max_dp[2])

    min_tmp[0] = a + min(min_dp[0], min_dp[1])
    min_tmp[1] = b + min(min_dp[0], min_dp[1], min_dp[2])
    min_tmp[2] = c + min(min_dp[1], min_dp[2])

    for i in range(3):
        max_dp[i] = max_tmp[i]
        min_dp[i] = min_tmp[i]

print(max(max_dp), min(min_dp))

"""
- 난이도: 골드5
- 분류: dp

- 주의: 메모리 제한이 4MB 이므로, 일반적인 2차원 dp로 풀면 메모리 초과가 발생한다.
"""
