# 캐슬 디펜스
from itertools import combinations
from collections import deque
from copy import deepcopy

N, M, D = map(int, input().split())
grid = deque(list(map(int, input().split())) for _ in range(N))

INF = int(1e9)
max_kills = 0


def calc_dist(pos1, pos2):
    r1, c1 = pos1
    r2, c2 = pos2
    return abs(r1 - r2) + abs(c1 - c2)


def shoot(grid, col, killed):
    min_dist = min_i = min_j = INF

    for i in range(N):
        for j in range(M):
            dist = calc_dist((i, j), (N, col))
            # 핵심1: "궁수는 사정거리 안에서 제일 가깝고 가장 왼쪽에 있는 적을 무조건 쏜다"
            if grid[i][j] == 1 and dist <= D:
                if dist < min_dist or (dist == min_dist and j < min_j):
                    min_dist = dist
                    min_i = i
                    min_j = j

    # 죽인 적을 기록
    if min_dist != INF:
        killed.add((min_i, min_j))


def simulate(grid, col1, col2, col3):
    kills = 0
    killed = set()

    for _ in range(N):
        # 각 궁수들이 화살을 쏨
        for col in [col1, col2, col3]:
            shoot(grid, col, killed)

        # 핵심2: 쏘면서 처리하지 말고 한번에 처리하기
        for i, j in killed:
            grid[i][j] = 0
            kills += 1
        killed.clear()

        # 다음 턴으로 진행 (데크로 처리)
        grid.pop()
        grid.appendleft([0] * M)

    return kills


for col1, col2, col3 in combinations(range(M), 3):
    max_kills = max(max_kills, simulate(deepcopy(grid), col1, col2, col3))

print(max_kills)

"""
- 난이도: 골드3
- 분류: 시뮬레이션, 브루트포스

디버깅
- 조건 미구현
    - 1. D 이하인 가장 가까운, 가장 왼쪽의 적이라는 조건을 제대로 고려하지 않았음 
    - 2. 핵심: "궁수들은 같은 적을 쏠 수 있다"
        -> 쏘면서 적을 지우면 안되고, 한번에 지우기
        -> 쏘면서 카운트를 세지 말고, 죽인 적을 기준으로 한번에 세기
- 멍청한 실수
    - 1. grid[i][j] == 1 조건을 빼먹었음
    - 2. 더 왼쪽에 있는거니까 j < min_j 로 해야 되는데 i < min_i로 했음

교훈
- 시키는대로 정확히 구현하자
    - ex. 궁수는 반드시 가장 가까운 맨 왼쪽을 쏴야 함, 죽인 적의 개수만 세야 됨
- 계획을 빠르게 검증하자
    - 어차피 실전에서는 하나만 선택해야 한다. (브루트포스 vs BFS)
- 모듈화는 나중에 하자
    - 일단 작성하면서 필요하면 그때 분리하자.
"""
