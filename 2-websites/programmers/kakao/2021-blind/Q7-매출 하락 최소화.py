import sys

sys.setrecursionlimit(10**6)

INF = int(1e9)
graph = [[] for _ in range(300001)]
dp = [[0] * 2 for _ in range(300001)]
sales_lst = []


def dfs(i):
    # base case
    if not graph[i]:
        dp[i][0], dp[i][1] = sales_lst[i], 0
        return

    # 초기값
    min_gap = INF
    dp[i][0] = sales_lst[i]

    # 자식에 대해 돌면서 계산
    for nxt in graph[i]:
        dfs(nxt)
        dp[i][0] += min(dp[nxt])
        min_gap = min(min_gap, dp[nxt][0] - dp[nxt][1])

    dp[i][1] = max(0, min_gap) + dp[i][0] - sales_lst[i]


def solution(sales, links):
    global sales_lst
    sales_lst = [0] + sales  # 1-idx

    for a, b in links:
        graph[a].append(b)

    dfs(1)
    return min(dp[1])


"""
- 분류: 트리 DP

dp[i][0]
- 의미: i번 노드가 루트인 서브트리에서 조건을 만족했을 때 매출합의 최소값, i번은 참석
- 계산: i번째 sales값 + (각 자식 노드들의 최소값)

dp[i][1]
- 의미: i번 노드가 루트인 서브트리에서 조건을 만족했을 때 매출합의 최소값, i번은 불참
- 계산: 자식 중에서 손해(참석의 비용)가 가장 적은 사람이 참석
"""
