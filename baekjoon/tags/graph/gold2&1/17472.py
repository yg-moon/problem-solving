# 다리 만들기 2
from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 각 섬을 색칠하는 함수
def number_islands(sx, sy, num):
    q = deque()
    q.append((sx, sy))
    while q:
        x, y = q.popleft()
        graph[x][y] = num
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
                q.append((nx, ny))


# 각 섬을 2,3,4,... 로 색칠
num = 2
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            number_islands(i, j, num)
            num += 1

# bridges[i][j]: 섬i와 섬j를 연결하는 다리의 비용
bridges = [[int(1e9)] * num for _ in range(num)]


# 현재 섬에서 출발하는 다리를 찾는 함수
def find_bridge(cur_land):
    starts = []
    for i in range(N):
        for j in range(M):
            if graph[i][j] == cur_land:
                starts.append((i, j))

    for x, y in starts:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dist = 0
            last = -1
            while 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 0:
                    dist += 1
                    nx += dx[i]
                    ny += dy[i]
                else:
                    last = graph[nx][ny]
                    break
            if dist >= 2 and last != -1:
                bridges[cur_land][last] = min(bridges[cur_land][last], dist)


# 모든 섬에서 출발하는 다리를 전부 찾기
for cur_land in range(2, num):
    find_bridge(cur_land)

# 이하 크루스칼
parent = list(range(num))
edges = []

for i in range(2, num):
    for j in range(2, num):
        if i != j and bridges[i][j] != int(1e9):
            edges.append((bridges[i][j], i, j))

edges.sort()


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


answer = 0
land_cnt = 1

for cost, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        land_cnt += 1
        answer += cost

if land_cnt == num - 2:
    print(answer)
else:
    print(-1)

"""
- 난이도: 골드1
- 분류: DFS/BFS + MST
- 소요 시간: 90분 (계획 10분, 구현 50분, 디버깅 30분)

요약
- 1. 각 섬을 2,3,4로 색칠
- 2. 각 섬에서 출발해서 다른 섬까지 연결되는 최소의 다리 찾기
    - 해당 섬의 모든 점을 시작점으로 넣고 출발
    - 상하좌우로 보면서, 다리가 완성되는지 확인 (길이2 이상)
- 3. 크루스칼 적용
    
디버깅: 1%에서 '틀렸습니다'
- 원인: 크루스칼을 union-find로 구현하지 않았음
- 이유: 단순 set으로는 cycle 확인이 불가능하므로, valid한 MST가 보장되지 않음
"""
