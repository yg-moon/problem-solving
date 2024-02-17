# 출처: https://sites.google.com/view/leejg/algorithm-test/프로그래머스-고득점-kit-파이썬-풀이/3-방의-개수
from collections import defaultdict


def solution(arrows):
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]

    visited = set([(0, 0)])
    edges = defaultdict(int)

    x, y = 0, 0
    answer = 0

    for d in arrows:
        for _ in range(2):
            nx, ny = x + dx[d], y + dy[d]
            if (nx, ny) in visited and edges[(x, y, nx, ny)] == 0:
                answer += 1
            edges[(x, y, nx, ny)] += 1
            edges[(nx, ny, x, y)] += 1
            visited.add((nx, ny))
            x, y = nx, ny

    return answer


"""
Approach
- 동일한 방을 여러번 카운트 하지 말아야 한다.
- 특정 노드에 두번 이상 반복하면 방이 만들어진다. 단, 구간 반복을 하는 경우를 제외한다.
- 모래시계의 형태를 위해서 한 번에 2칸씩 움직여서 Center를 거치도록 한다.(모래 시계 형태 Count +2)
- 새로운 방이 생기는 조건
    - 1. Node에 2번 이상 방문할 때
    - 2. 방문하는 경로가 새로운 경로로 방문(N개의 Node간 반복해서 왕복할 때 Count 하지 않기 위해)
"""
