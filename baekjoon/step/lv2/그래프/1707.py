# 이분 그래프
# 출처: https://ji-gwang.tistory.com/293
from collections import defaultdict, deque
import sys

input = sys.stdin.readline


def bfs(start, group):
    q = deque([start])
    visited[start] = group
    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            # 방문하지 않은 노드면 그룹 색을 반전시켜서 저장
            if visited[nxt] == 0:
                visited[nxt] = -visited[cur]  # 주의: 여기서 -group이 아님
                q.append(nxt)
            # 이미 방문한 노드인데 색이 같다면 이분 그래프가 아님
            elif visited[nxt] == visited[cur]:
                return False
    return True


K = int(input())

for _ in range(K):
    graph = defaultdict(list)
    V, E = map(int, input().split())
    visited = [0] * (V + 1)  # 0: 미방문, 1: 그룹1, -1: 그룹2

    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    # 모든 노드에 대해, 미방문인 경우 BFS 수행
    for i in range(1, V + 1):
        if visited[i] == 0:
            is_bipartite = bfs(i, 1)
            if not is_bipartite:
                break

    print("YES" if is_bipartite else "NO")

"""
- 난이도: 골드4
- 분류: BFS

핵심
- 이분 그래프는 BFS로 탐색하면 매 층마다 색이 반전되어야 한다. 
"""
