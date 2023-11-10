# 감시
from copy import deepcopy

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 팁: 이렇게 하면 방향정보를 깔끔하게 저장할 수 있음
cam_dirs_dict = {
    1: [[0], [1], [2], [3]],
    2: [[0, 2], [1, 3]],
    3: [[0, 1], [1, 2], [2, 3], [0, 3]],
    4: [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
    5: [[0, 1, 2, 3]],
}

# CCTV 정보
cam_info = []
for i in range(N):
    for j in range(M):
        if graph[i][j] in range(1, 6):
            cam_info.append((graph[i][j], i, j))

min_cnt = int(1e9)


def get_count(graph):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                cnt += 1
    return cnt


def draw(x, y, dirs, graph):
    for dir in dirs:
        nx = x + dx[dir]
        ny = y + dy[dir]
        while 0 <= nx < N and 0 <= ny < M and graph[nx][ny] != 6:
            if graph[nx][ny] == 0:
                graph[nx][ny] = "#"
            nx += dx[dir]
            ny += dy[dir]


def dfs(depth, graph):
    global min_cnt

    if depth == len(cam_info):
        min_cnt = min(min_cnt, get_count(graph))
        return

    cam, x, y = cam_info[depth]

    for i in range(len(cam_dirs_dict[cam])):
        new_graph = deepcopy(graph)
        draw(x, y, cam_dirs_dict[cam][i], new_graph)
        dfs(depth + 1, new_graph)


dfs(0, graph)

print(min_cnt)

"""
- 난이도: 골드4
- 분류: 시뮬레이션, 백트래킹

- 요약: 각 카메라마다 특정 방향인 경우를 가정하고 그리기
- 디버깅: "CCTV는 CCTV를 통과할 수 있다."
"""
