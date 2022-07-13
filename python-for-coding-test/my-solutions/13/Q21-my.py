from copy import deepcopy
from collections import defaultdict, deque

N, L, R = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

zeros = [[0] * N for _ in range(N)]
unions = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, n):
    Q = deque([[x, y]])
    unions[x][y] = n
    while Q:
        curr_x, curr_y = Q.popleft()
        for i in range(4):
            nx = curr_x + dx[i]
            ny = curr_y + dy[i]
            if (
                0 <= nx < N
                and 0 <= ny < N
                and unions[nx][ny] == 0
                and L <= abs(graph[curr_x][curr_y] - graph[nx][ny]) <= R
            ):
                unions[nx][ny] = n
                Q.append([nx, ny])


cnt = 0
while True:
    unions = deepcopy(zeros)
    ally_num = 0
    for x in range(N):
        for y in range(N):
            if unions[x][y] == 0:
                # 연합 만들기
                ally_num += 1
                bfs(x, y, ally_num)
    # 아무 연합이 없으면 종료
    if ally_num == N * N:
        break
    # 각 연합의 총합 / 개수 / 평균 구하기
    ally_sum = defaultdict(int)
    ally_cnt = defaultdict(int)
    ally_mean = defaultdict(int)
    for x in range(N):
        for y in range(N):
            ally_sum[unions[x][y]] += graph[x][y]
            ally_cnt[unions[x][y]] += 1
    for key in ally_sum:
        mean = ally_sum[key] // ally_cnt[key]
        ally_mean[key] = mean
    # 각 연합에 속하는 칸은 평균 인원으로 변경
    for x in range(N):
        for y in range(N):
            if unions[x][y] in ally_mean:
                graph[x][y] = ally_mean[unions[x][y]]
    # 인구 이동 횟수 증가
    cnt += 1

print(cnt)
