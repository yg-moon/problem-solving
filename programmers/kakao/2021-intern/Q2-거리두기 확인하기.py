from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


# 현재 위치의 응시자가 거리두기를 지키는지 확인
def bfs(graph, i, j):
    q = deque()
    q.append((i, j, 0, "S"))
    visited = [[False] * 5 for _ in range(5)]
    visited[i][j] = True

    while q:
        x, y, dist, item = q.popleft()
        if dist <= 2 and item == "P":
            return False
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (
                0 <= nx < 5
                and 0 <= ny < 5
                and graph[nx][ny] != "X"
                and not visited[nx][ny]
            ):
                visited[nx][ny] = True
                q.append((nx, ny, dist + 1, graph[nx][ny]))

    return True


# 대기실의 모든 응시자가 거리두기를 지키는지 확인
def check(graph):
    for i in range(5):
        for j in range(5):
            if graph[i][j] == "P":
                if not bfs(graph, i, j):
                    return False
    return True


def solution(places):
    answer = []

    for place in places:
        # 각 대기실을 2차원 배열로 변경
        graph = []
        for row in place:
            graph.append(list(row))

        if check(graph):
            answer.append(1)
        else:
            answer.append(0)

    return answer


"""
- 분류: BFS
- 소요 시간: 6:20-6:50 (30분)

구현 디테일
- 2중 for문 한번에 탈출 -> 함수로 분리해서 리턴

디버깅
- 답이 틀림
    - 원인: BFS 초기지점 방문처리를 해주지 않았음
"""
