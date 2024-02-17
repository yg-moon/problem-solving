# 치즈
from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

time = 0


# 공기가 있는 칸을 찾기
def get_air(graph):
    q = deque()
    q.append((0, 0))
    visited = [[False] * M for _ in range(N)]
    visited[0][0] = True

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (
                0 <= nx < N
                and 0 <= ny < M
                and graph[nx][ny] == 0
                and not visited[nx][ny]
            ):
                visited[nx][ny] = True
                q.append((nx, ny))

    return visited


# 공기와 닿은 치즈가 녹음
def get_next_state(graph, air):
    ret = [[0] * M for _ in range(N)]
    prev_cnt = 0
    cur_cnt = 0

    for x in range(N):
        for y in range(M):
            if graph[x][y] == 0:
                ret[x][y] = 0
            else:
                prev_cnt += 1
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < N and 0 <= ny < M and air[nx][ny]:
                        ret[x][y] = 0
                        break
                else:
                    ret[x][y] = 1
                    cur_cnt += 1

    return [ret, prev_cnt, cur_cnt]


# 시간에 따라 시뮬레이션
while True:
    time += 1
    graph, prev, cur = get_next_state(graph, get_air(graph))
    if cur == 0:
        break

print(time)
print(prev)

"""
- 난이도: 골드4
- 분류: DFS/BFS
- 소요 시간: 40분 (디버깅도 안 했는데 오래 걸렸네)

핵심
- 치즈구멍 속에는 공기가 없으므로, (0,0)에서 BFS로 연결된 것만 공기로 생각
- 매번 치즈 칸의 개수를 추적해서, 모두 녹기 직전의 개수를 출력
"""
