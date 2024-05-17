# 열쇠
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    global answer

    q = deque([[0, 0]])
    visited = [[False] * (W + 2) for _ in range(H + 2)]
    visited[0][0] = True

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위를 벗어나거나 벽이거나 이미 방문했다면 컨티뉴
            if not (
                0 <= nx < H + 2
                and 0 <= ny < W + 2
                and graph[nx][ny] != "*"
                and not visited[nx][ny]
            ):
                continue

            # 문
            if "A" <= graph[nx][ny] <= "Z":
                if graph[nx][ny].lower() not in keys:
                    continue
            # 열쇠
            elif "a" <= graph[nx][ny] <= "z":
                if graph[nx][ny] not in keys:
                    keys.add(graph[nx][ny])
                    # 핵심2: 새 열쇠를 찾으면 방문배열을 리셋
                    visited = [[False] * (W + 2) for _ in range(H + 2)]
            # 문서
            elif graph[nx][ny] == "$":
                if (nx, ny) not in visited_doc:
                    answer += 1
                    visited_doc.append((nx, ny))

            visited[nx][ny] = True
            q.append([nx, ny])


T = int(input())

for _ in range(T):
    H, W = map(int, input().split())

    # 핵심1: 외곽을 한칸 패딩
    graph = [["."] * (W + 2) for _ in range(H + 2)]
    building = [list(input()) for _ in range(H)]
    for i in range(H):
        for j in range(W):
            graph[i + 1][j + 1] = building[i][j]

    keys = set(input())
    if keys == {"0"}:
        keys = set()

    answer = 0
    visited_doc = []
    bfs()
    print(answer)

"""
- 난이도: 골드1
- 분류: 구현, BFS

핵심
- 1. 외곽에 "."으로 한칸 패딩하고 (0,0)에서 BFS를 시작하면, 입구를 따로 구할 필요가 없음
- 2. 새로운 열쇠를 찾으면 방문배열을 리셋
- 3. 문서위치는 따로 기록해서 중복계산을 방지

참고
- https://ji-gwang.tistory.com/449
"""
