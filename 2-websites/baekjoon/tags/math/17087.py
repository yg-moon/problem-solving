# 숨바꼭질 6
import math

N, S = map(int, input().split())
arr = list(map(int, input().split()))

# 수빈이와 각 동생간의 거리
dist = []
for a in arr:
    dist.append(abs(S - a))

# GCD
answer = dist[0]
for i in range(1, N):
    answer = math.gcd(answer, dist[i])
print(answer)

"""
- 난이도: 실버2
- 분류: 수학

풀이
- 오답: 인접한 지점간의 거리중 최솟값 구하기
- 정답: 수빈이와 모든 동생간의 최대공약수 구하기
"""
