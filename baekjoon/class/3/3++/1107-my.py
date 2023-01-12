# 리모컨
import sys

sys.setrecursionlimit(10**6)

N = int(input())
M = int(input())
broken = []
if M != 0:
    broken = list(map(int, input().split()))

nums = [x for x in range(10) if x not in broken]
min_move = abs(N - 100)
limit = N + abs(N - 100)


def solve(num_str):
    global min_move, limit
    if num_str != "":
        min_move = min(min_move, len(num_str) + abs(N - int(num_str)))
        if int(num_str) > limit or int(num_str) == 0:
            return
    for i in range(len(nums)):
        solve(num_str + str(nums[i]))


solve("")

print(min_move)

"""
- 난이도: 골드5
- 분류: 브루트포스

핵심
- 탐색 방식: 가능한 후보중에서 한글자씩 늘려가면서, '글자길이 + abs(N - 현재숫자)'의 최솟값을 갱신.
- 최대 범위: N + abs(N - 100)까지. (그 이상은 만들어도 +/- 눌러서 가는게 더 빠르므로)
"""
