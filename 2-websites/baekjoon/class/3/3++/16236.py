# 아기 상어
from collections import deque

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

shark_size = 2
grow_cnt = 0
time = 0

# 상어 초기위치
for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            shark_x = i
            shark_y = j


def bfs(start_x, start_y):
    q = deque([[start_x, start_y]])
    dist = [[-1] * N for _ in range(N)]
    dist[start_x][start_y] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (
                0 <= nx < N
                and 0 <= ny < N
                and graph[nx][ny] <= shark_size
                and dist[nx][ny] == -1
            ):
                dist[nx][ny] = dist[x][y] + 1
                q.append([nx, ny])
    return dist


# 먹을 수 있는 물고기의 좌표
def find_eatable():
    pos = []
    for i in range(N):
        for j in range(N):
            if graph[i][j] != 0 and graph[i][j] != 9 and graph[i][j] < shark_size:
                pos.append((i, j))
    return pos


while True:
    # 후보 찾기
    pos = find_eatable()
    # 후보가 없으면 종료
    if not pos:
        break

    dist = bfs(shark_x, shark_y)
    nx = 0
    ny = 0
    cur_d = 0

    # 후보가 한마리 일 때
    if len(pos) == 1:
        nx = pos[0][0]
        ny = pos[0][1]
        cur_d = dist[nx][ny]
        if cur_d == -1:
            break
    # 후보가 여러 마리 일 때
    else:
        # 후보 물고기마다 거리를 파악
        d_info = []
        for x, y in pos:
            d_info.append(dist[x][y])
        # 먹을 수 있는게 없으면 종료
        max_dist = max(d_info)
        if max_dist == -1:
            break
        # 가장 가까운 물고기의 위치 선택
        min_dist = int(1e9)
        idx = 0
        for i in range(len(d_info)):
            if d_info[i] != -1 and d_info[i] < min_dist:
                idx = i
                min_dist = d_info[i]
        nx, ny = pos[idx]
        cur_d = min_dist

    # 먹기
    # 상어 이동
    graph[shark_x][shark_y] = 0
    graph[nx][ny] = 9
    shark_x, shark_y = nx, ny
    # 시간 추가
    time += cur_d
    # 크기 갱신
    grow_cnt += 1
    if grow_cnt == shark_size:
        shark_size += 1
        grow_cnt = 0

print(time)

"""
- 난이도: 골드3
- 분류: 시뮬레이션
"""
