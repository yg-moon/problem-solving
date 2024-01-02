# 맥주 마시면서 걸어가기
from collections import deque


def get_dist(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)


def bfs():
    q = deque()
    q.append((home_x, home_y))
    visited = [False] * len(conv)
    is_possible = False

    while q:
        x, y = q.popleft()

        if x == fest_x and y == fest_y:
            is_possible = True
            break

        for i in range(len(conv)):
            nx, ny = conv[i][0], conv[i][1]
            div, mod = divmod(get_dist(x, y, nx, ny), 50)
            if mod != 0:
                div += 1
            if div <= 20 and not visited[i]:
                q.append((nx, ny))
                visited[i] = True

    if is_possible:
        print("happy")
    else:
        print("sad")


T = int(input())

for _ in range(T):
    N = int(input())
    home_x, home_y = map(int, input().split())
    conv = [list(map(int, input().split())) for _ in range(N)]
    fest_x, fest_y = map(int, input().split())
    conv.append([fest_x, fest_y])
    bfs()

"""
- 난이도: 골드5
- 분류: BFS
- 소요 시간: 40분 (1차 15분, 2차 25분)

1차 시도: 틀렸습니다
- 이유1: 주어진 좌표대로 방문순서일 것이라고 착각했다.
- 이유2: 모든 편의점을 방문해야 한다고 착각했다.
- (문제 이해를 잘하자!)

2차 시도: BFS를 이용
- 어떻게든 집 -> 편의점들 -> 페스티벌 순서로 도착하면 됨
- 매번 도달 가능한 모든 좌표를 전부 탐방해보고, 그 중 하나라도 성공하면 됨
- (주의: 최단거리로 이동하는 것이 아님)
"""
