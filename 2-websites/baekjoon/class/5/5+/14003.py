# 가장 긴 증가하는 부분 수열 5
# 출처: https://my-coding-notes.tistory.com/270
import sys, bisect

INF = sys.maxsize  # 주의: -10억이 100만개 들어올 수 있으므로, 아주 큰 수가 필요

N = int(input())
arr = [0] + list(map(int, input().split()))  # 1-idx
dp = [0] * (N + 1)
LIS = [-INF]  # 주의: 문제에서 음수가 허용되므로 0이 아니라 -INF부터 시작

# LIS
for i in range(1, N + 1):
    if LIS[-1] < arr[i]:
        LIS.append(arr[i])
        dp[i] = len(LIS) - 1
    else:
        dp[i] = bisect.bisect_left(LIS, arr[i])
        LIS[dp[i]] = arr[i]
print(len(LIS) - 1)

# 역추적
answer = []
max_idx = max(dp)
for i in range(N, 0, -1):
    if dp[i] == max_idx:
        answer.append(arr[i])
        max_idx -= 1
print(*answer[::-1])

"""
- 난이도: 플래5
- 분류: 이분탐색

- LIS O(nlogn), 최적해 출력
"""
