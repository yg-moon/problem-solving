INF = int(1e9)


def solution(n, results):
    graph = [[INF] * (n + 1) for _ in range(n + 1)]

    # 자기 자신에게 가는 비용은 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                graph[i][j] = 0

    # 주의: 순위를 결정할 때 승패 여부는 중요하므로 단방향 그래프로 입력
    for a, b in results:
        graph[a][b] = 1

    # 플로이드 워셜
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    # 모든 선수와 연결되어 있으면 정답+1
    answer = 0
    for i in range(1, n + 1):
        cnt = 0
        for j in range(1, n + 1):
            if graph[i][j] != INF or graph[j][i] != INF:
                cnt += 1
        if cnt == n:
            answer += 1
    return answer


"""
- 요약: 플로이드 배열에서 한 방향만이라도 모든 학생과 연결되어 있다면 정확한 순위를 알 수 있다.
- 이유: 선수A에서 선수B로 가는 최단거리 문제로 생각시, 경로가 존재한다면 순위 비교가 가능한 것이므로.
"""
