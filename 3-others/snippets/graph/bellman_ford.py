# BOJ 11657
INF = int(1e9)

N, M = map(int, input().split())
edges = []
dist = [INF] * (N + 1)

for _ in range(M):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))
    # 팁: 인접리스트 방식의 graph 대신 이렇게 edge만 다룰수도 있음


def bellman_ford(start):
    dist[start] = 0
    for i in range(N):  # n번 반복
        for edge in edges:  # 매 반복마다 모든 간선을 확인
            cur, nxt, cost = edge
            # 현재 간선을 거치는게 더 짧으면 갱신
            if dist[cur] != INF and dist[nxt] > dist[cur] + cost:
                dist[nxt] = dist[cur] + cost
                # n번째 반복에서도 값이 갱신되면 negative cycle이 존재
                if i == N - 1:
                    return True
    return False


negative_cycle = bellman_ford(1)

if negative_cycle:
    print("-1")
else:
    for i in range(2, N + 1):
        if dist[i] == INF:
            print("-1")
        else:
            print(dist[i])

"""
특징
- 음수 간선이 존재할 때 사용
- 음수 간선의 순환을 감지할 수 있음
- 시간복잡도: O(VE)

동작 과정
- 시작 노드에 대해서 거리를 0으로 초기화, 나머지 노드는 거리를 무한으로 설정
- n-1번 만큼 다음 과정을 반복
    - 매 반복 마다 모든 간선을 확인 (다익스트라와의 차이점)
    - 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우, 거리 정보 갱신
    - n-1번 반복 이후, n번째 반복에서도 거리 값이 갱신된다면 음수 순환이 존재
"""
