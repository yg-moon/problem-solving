N = 0
INF = int(1e9)


def floyd(fares):
    dist = [[INF] * (N + 1) for _ in range(N + 1)]

    # 자기 자신은 0
    for i in range(1, N + 1):
        dist[i][i] = 0

    for u, v, w in fares:
        dist[u][v] = w
        dist[v][u] = w

    # 주의: 바깥 루프를 k부터 시작
    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist


def solution(n, s, a, b, fares):
    global N
    N = n
    answer = INF

    dist = floyd(fares)

    for x in range(1, N + 1):
        answer = min(answer, dist[s][x] + dist[x][a] + dist[x][b])

    return answer


"""
- 플로이드-워셜 풀이 (O(V^3))
"""
