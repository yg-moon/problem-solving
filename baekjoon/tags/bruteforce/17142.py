# 연구소 3
from itertools import combinations
from collections import deque
from copy import deepcopy

INF = int(1e9)

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

virus_pos = []
empty_cnt = 0
min_time = INF

# 그래프 표기 변경, 바이러스 후보위치 수집
for i in range(N):
    for j in range(N):
        if graph[i][j] == 0:  # 빈칸
            empty_cnt += 1
        elif graph[i][j] == 1:  # 벽
            graph[i][j] = "-"
        elif graph[i][j] == 2:  # 바이러스
            graph[i][j] = "*"
            virus_pos.append((i, j))


def simulate(graph):
    global empty_cnt
    q = deque()
    visited = [[False] * N for _ in range(N)]
    cnt = 0

    # 시작위치 처리
    for i in range(N):
        for j in range(N):
            if graph[i][j] == "#":
                q.append((i, j, 0))
                visited[i][j] = True

    # BFS
    while q:
        x, y, val = q.popleft()

        # 효율성1: 기존 정답보다 크다면 조기종료
        if min_time < val:
            break

        # 효율성2: 바이러스가 다 퍼졌는지 확인
        if empty_cnt == cnt:
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (
                0 <= nx < N
                and 0 <= ny < N
                and graph[nx][ny] != "-"
                and not visited[nx][ny]
            ):
                # 다음 위치가 빈칸일 때
                if graph[nx][ny] != "*":
                    cnt += 1
                # 현재 위치가 출발점일 때
                if graph[x][y] == "#":
                    graph[nx][ny] = 1
                else:
                    graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny, graph[nx][ny]))
                visited[nx][ny] = True

    # 바이러스가 다 퍼졌는지 확인
    if empty_cnt != cnt:
        return INF

    # 현재 그래프에서 최댓값 찾기
    max_val = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] not in ["-", "*", "#"]:
                max_val = max(max_val, graph[i][j])
    return max_val


# 모든 조합에 대해 실행
for comb in combinations(virus_pos, M):
    new_graph = deepcopy(graph)
    for i, j in comb:
        new_graph[i][j] = "#"  # 활성화된 바이러스
    min_time = min(min_time, simulate(new_graph))

if min_time != INF:
    print(min_time)
else:
    print(-1)

"""
- 난이도: 골드3
- 분류: 시뮬레이션, 브루트포스, BFS

요약
- M개의 활성 바이러스를 두는 모든 조합에 대해 시뮬레이션
- 거리와 구조물을 구분하기 위해 그래프의 표기법을 변경 (or 거리는 visited로 관리하는 방식도 가능)

조건
- 비활성 바이러스도 닿으면 활성으로 변함
- 빈칸만 다 채워지면 그 즉시 종료해야함

디버깅
- 시간초과 
    - 원인: 끝났는지 검사할 때 매번 전체를 탐색하는게 비효율적 (2차원 배열 탐색)
    - 해결: 전체 빈칸개수와 현재 채운개수를 카운팅해서 비교 (정수값으로 추적)
"""
