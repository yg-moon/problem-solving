# BOJ 16236
import heapq

# 입력
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

# 필요 변수
INF = int(1e9)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
shark_size = 2
grow_cnt = 0
time = 0
for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            shark_x = i
            shark_y = j

# 다익스트라: 이코테 버전
def dijk(start_x, start_y):
    dist = [[INF] * N for _ in range(N)]
    dist[start_x][start_y] = 0
    Q = [(0, start_x, start_y)]
    while Q:
        time, x, y = heapq.heappop(Q)
        # 처리된 적이 있으면 스킵
        if dist[x][y] < time:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] <= shark_size:
                alt = time + 1
                # relaxation
                if alt < dist[nx][ny]:
                    dist[nx][ny] = alt
                    heapq.heappush(Q, (alt, nx, ny))
    return dist


# 먹을 수 있는 물고기의 좌표
def find_eatable():
    pos = []
    for i in range(N):
        for j in range(N):
            if graph[i][j] != 0 and graph[i][j] != 9 and graph[i][j] < shark_size:
                pos.append((i, j))
    return pos


# 메인 로직
while True:
    # 후보 찾기
    pos = find_eatable()

    # 후보가 없으면 종료
    if not pos:
        break

    # 필요 변수
    dist = dijk(shark_x, shark_y)
    nx = 0
    ny = 0
    curr_d = 0

    # 후보가 한마리 일 때
    if len(pos) == 1:
        nx = pos[0][0]
        ny = pos[0][1]
        curr_d = dist[nx][ny]
        if curr_d == INF:
            break
    # 후보가 여러 마리 일 때
    else:
        # 후보 물고기마다 거리를 파악
        d_info = []
        for x, y in pos:
            d_info.append(dist[x][y])
        # 먹을 수 있는게 없으면 종료
        min_dist = min(d_info)
        if min_dist == INF:
            break
        # 가장 가까운 물고기의 위치 선택
        for i in range(len(d_info)):
            if d_info[i] == min_dist:
                nx, ny = pos[i]
                curr_d = min_dist
                break

    # 먹기
    # 상어 이동
    graph[shark_x][shark_y] = 0
    graph[nx][ny] = 9
    shark_x, shark_y = nx, ny
    # 시간 추가
    time += curr_d
    # 크기 갱신
    grow_cnt += 1
    if grow_cnt == shark_size:
        shark_size += 1
        grow_cnt = 0


print(time)
