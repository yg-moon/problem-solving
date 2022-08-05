# BOJ 16234
# 출처: 이코테
from collections import deque

N, L, R = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


# 연합을 형성하고 인구 이동
def unite_and_move(x, y, union_num):
    united = []  # (x, y)의 위치와 연결된 나라(연합) 정보를 담는 리스트
    united.append((x, y))
    union_total = graph[x][y]  # 현재 연합의 전체 인구 수
    nation_cnt = 1  # 현재 연합의 국가 수

    # BFS
    Q = deque()
    Q.append((x, y))
    union[x][y] = union_num  # 현재 연합의 번호 할당
    while Q:
        curr_x, curr_y = Q.popleft()
        for i in range(4):
            nx = curr_x + dx[i]
            ny = curr_y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and union[nx][ny] == -1:
                if L <= abs(graph[nx][ny] - graph[curr_x][curr_y]) <= R:
                    Q.append((nx, ny))
                    # 연합에 추가하기
                    union[nx][ny] = union_num
                    union_total += graph[nx][ny]
                    nation_cnt += 1
                    united.append((nx, ny))
    # 연합 국가끼리 인구를 분배
    for i, j in united:
        graph[i][j] = union_total // nation_cnt


total_count = 0
while True:
    union = [[-1] * N for _ in range(N)]
    union_num = 0
    for i in range(N):
        for j in range(N):
            # 해당 나라가 아직 처리되지 않았다면
            if union[i][j] == -1:
                unite_and_move(i, j, union_num)
                union_num += 1
    # 아무 연합이 없으면 종료 (모든 인구 이동이 끝난 경우)
    if union_num == N * N:
        break
    total_count += 1

print(total_count)
