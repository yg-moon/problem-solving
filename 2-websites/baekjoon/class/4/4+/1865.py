# 웜홀
# 출처: https://backtony.github.io/algorithm/2021-02-13-algorithm-boj-class4-10/
def bellman_ford(start):
    dist = [INF] * (N + 1)
    dist[start] = 0
    for i in range(N):  # n번 반복
        for edge in edges:  # 매번 모든 간선을 확인
            cur, nxt, cost = edge
            # 핵심: dist[cur] != INF 조건을 삭제 (시작점과 관계없이 진행하도록)
            if dist[nxt] > dist[cur] + cost:  # relaxation
                dist[nxt] = dist[cur] + cost
                if i == N - 1:  # n번째 반복에서도 갱신되면 음의 사이클이 존재
                    return True
    return False


INF = int(1e9)
TC = int(input())

for _ in range(TC):
    N, M, W = map(int, input().split())
    edges = []

    for _ in range(M):
        S, E, T = map(int, input().split())
        # 인접리스트 그래프 대신 이렇게 간선만으로도 풀이 가능
        edges.append((S, E, T))
        edges.append((E, S, T))

    for _ in range(W):
        S, E, T = map(int, input().split())
        # 웜홀을 따로 만들 필요없이 음수 간선으로 추가하면 됨
        edges.append((S, E, -T))

    negative_cycle = bellman_ford(1)

    if negative_cycle:
        print("YES")
    else:
        print("NO")

"""
- 난이도: 골드3
- 분류: 벨만-포드

핵심
- 시작점에 관계없이 음의 사이클만 확인하면 되는 문제다.
    - 주의: 모든 지점을 시작점으로 두는 방식으로 해결하면 안 된다. (시간초과)
    - 해결: dist[cur] != INF 조건을 삭제하면 된다.
        - 이렇게 하면 시작점과 무관하게 진행되고, n번째 반복에서 사이클 여부를 판단할 수 있다.
"""
