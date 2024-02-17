# 사회망 서비스(SNS)
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

# dp[i][j]: i번 노드의 상태가 j일때(j==1이면 얼리어답터), 서브트리에서 얼리어답터인 노드의 개수
dp = [[0] * 2 for _ in range(N + 1)]
visited = [False] * (N + 1)


def dfs(node):
    visited[node] = True
    dp[node][1] = 1  # 본인이 얼리면 서브트리도 +1

    for nxt in tree[node]:
        if visited[nxt]:
            continue
        dfs(nxt)
        dp[node][0] += dp[nxt][1]  # 1. 부모가 얼리어답터가 아닌 경우, 자식은 얼리어답터여야함
        dp[node][1] += min(dp[nxt])  # 2. 부모가 얼리어답터인 경우, 자식은 상관없음


dfs(1)

print(min(dp[1]))

"""
- 난이도: 골드3
- 분류: dp

- 요약: 트리dp 유형
- 참고: https://thought-process-ing.tistory.com/337
"""
