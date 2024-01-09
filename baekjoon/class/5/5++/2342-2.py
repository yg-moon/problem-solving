import sys

sys.setrecursionlimit(10**6)

arr = list(map(int, input().split()))

arr.pop()
N = len(arr)

# dp[지시사항 순서][왼발 위치][오른발 위치]: 여기서 '시작'했을때 모든 지시사항을 만족하는 최소의 힘
dp = [[[-1] * 5 for _ in range(5)] for _ in range(N + 1)]


def get_cost(start, end):
    if start == end:
        return 1
    elif start == 0:
        return 2
    elif abs(start - end) % 2 != 0:
        return 3
    else:
        return 4


def dfs(i, l, r):
    # Base case
    if i >= N:
        return 0

    # Memoization
    if dp[i][l][r] != -1:
        return dp[i][l][r]

    # Recursion
    nxt = arr[i]
    dp[i][l][r] = min(
        dfs(i + 1, nxt, r) + get_cost(l, nxt),  # 왼발을 움직인 경우
        dfs(i + 1, l, nxt) + get_cost(r, nxt),  # 오른발을 움직인 경우
    )

    return dp[i][l][r]


print(dfs(0, 0, 0))

"""
- 탑다운 풀이
- 출처: https://0902.tistory.com/41
"""
