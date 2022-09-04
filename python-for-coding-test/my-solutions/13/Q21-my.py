# BOJ 16234
# 인구 재조정을 따로 처리하여 비효율적
from collections import defaultdict, deque

N, L, R = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

unions = []  # 연합 상태를 나타낼 2차원 배열
cnt = 0  # 총 인구이동 횟수

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, num):
    Q = deque([[x, y]])
    unions[x][y] = num
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
                unions[nx][ny] = num
                Q.append([nx, ny])


while True:
    unions = [[0] * N for _ in range(N)]  # 연합 상태는 매번 초기화
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
