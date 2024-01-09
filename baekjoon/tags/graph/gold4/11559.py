# Puyo Puyo
from collections import deque

graph = [list(input()) for _ in range(12)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

answer = 0


# graph1에 graph2를 반영
def add_record(graph1, graph2):
    for i in range(12):
        for j in range(6):
            if graph2[i][j]:
                graph1[i][j] = True


# 뿌요 덩어리 찾기
def bfs(sx, sy):
    q = deque()
    q.append((sx, sy))
    visited[sx][sy] = True
    cur_visited[sx][sy] = True
    puyo_cnt = 0

    while q:
        x, y = q.popleft()

        puyo_cnt += 1
        visited[x][y] = True
        cur_visited[x][y] = True

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (
                0 <= nx < 12
                and 0 <= ny < 6
                and graph[nx][ny] == graph[sx][sy]
                and not visited[nx][ny]  # 주의: 항상 방문여부 확인하기
            ):
                visited[nx][ny] = True
                cur_visited[nx][ny] = True
                q.append((nx, ny))

    return puyo_cnt


def get_next_graph(graph, will_pop):
    # 터뜨리기
    for i in range(12):
        for j in range(6):
            if will_pop[i][j]:
                graph[i][j] = "."

    # 중력에 의한 떨어짐
    # 구현: 각 열마다 맨밑 한칸 위에서 시작, 자신 밑에 빈칸이 없을 때까지 스왑
    for j in range(6):
        for i in range(10, -1, -1):
            cur = i
            while cur <= 10:
                if graph[cur][j] != "." and graph[cur + 1][j] == ".":
                    graph[cur][j], graph[cur + 1][j] = (
                        graph[cur + 1][j],
                        graph[cur][j],
                    )  # swap
                    cur += 1
                else:
                    break

    return graph


while True:
    visited = [[False] * 6 for _ in range(12)]
    will_pop = [[False] * 6 for _ in range(12)]
    group_cnt = 0

    # 메인 로직
    for i in range(12):
        for j in range(6):
            if graph[i][j] != "." and not visited[i][j]:
                cur_visited = [[False] * 6 for _ in range(12)]
                puyo_cnt = bfs(i, j)
                if puyo_cnt >= 4:
                    group_cnt += 1
                    add_record(will_pop, cur_visited)

    if group_cnt == 0:
        break

    answer += 1
    graph = get_next_graph(graph, will_pop)

print(answer)

"""
- 난이도: 골드4
- 분류: DFS/BFS
- 소요 시간: 40분

요약
- 현재 상태에서 4개 이상 연결된 것들을 찾고, 전부 터뜨림
- 중력에 의해 남은 뿌요들은 떨어짐
- 더 이상 터질게 없으면 종료

핵심
- 현재 상황에서 터뜨리기 구현 (cur_visited, will_pop 활용)
- 중력에 의한 떨어짐 구현
"""
