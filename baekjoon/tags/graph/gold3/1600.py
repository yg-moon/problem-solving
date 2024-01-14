# 말이 되고픈 원숭이
from collections import deque

K = int(input())
W, H = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(H)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
hx = [-1, -2, -2, -1, 1, 2, 2, 1]
hy = [-2, -1, 1, 2, -2, -1, 1, 2]


def bfs():
    q = deque()
    q.append((0, 0, 0))

    # 핵심: dist[z][x][y] -> 능력을 z번 사용했을때 (x,y) 방문여부 및 거리
    dist = [[[-1] * W for _ in range(H)] for _ in range(K + 1)]
    dist[0][0][0] = 0

    while q:
        x, y, cur_k = q.popleft()

        if x == H - 1 and y == W - 1:
            return dist[cur_k][x][y]

        # 상하좌우 이동
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (
                0 <= nx < H
                and 0 <= ny < W
                and graph[nx][ny] == 0
                and dist[cur_k][nx][ny] == -1
            ):
                q.append((nx, ny, cur_k))
                dist[cur_k][nx][ny] = dist[cur_k][x][y] + 1

        # 말처럼 이동
        if cur_k < K:
            for i in range(8):
                nx = x + hx[i]
                ny = y + hy[i]
                # 주의: if문이 스코프를 벗어나 있었음
                if (
                    0 <= nx < H
                    and 0 <= ny < W
                    and graph[nx][ny] == 0
                    and dist[cur_k + 1][nx][ny] == -1
                ):
                    q.append((nx, ny, cur_k + 1))
                    dist[cur_k + 1][nx][ny] = dist[cur_k][x][y] + 1

    return -1


print(bfs())

"""
- 난이도: 골드3
- 분류: BFS
- 소요 시간: 45분 (풀이 25분, 디버깅 20분)

- 요약: BFS로 최단거리를 찾는데, K번만큼 말처럼 움직일 수 있음
- 핵심: 능력을 몇 번 사용해서 해당 위치에 도착한 것인지 구분하기
"""
