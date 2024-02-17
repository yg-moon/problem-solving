# 탈출
from collections import deque

R, C = map(int, input().split())
graph = [list(input()) for _ in range(R)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

wq = deque()  # 물의 위치를 저장할 큐

# 시작점, 도착점, 물의 위치
for x in range(R):
    for y in range(C):
        if graph[x][y] == "S":
            Sx, Sy = x, y
            graph[x][y] = "."  # 팁: 시작점은 빈칸으로 변경
        elif graph[x][y] == "D":
            Dx, Dy = x, y
        elif graph[x][y] == "*":
            wq.append((x, y))


# 물 퍼뜨리기
def water():
    # 핵심: 매번 현재 큐에 있는 만큼만 실행 (현재 상태까지만 진행)
    q_len = len(wq)
    while q_len:
        x, y = wq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] == ".":
                graph[nx][ny] = "*"
                wq.append((nx, ny))
        q_len -= 1


# (고슴도치 이동 -> 물 퍼뜨리기)를 반복
def bfs():
    q = deque()
    q.append((Sx, Sy))
    dist = [[-1] * C for _ in range(R)]
    dist[Sx][Sy] = 0

    while q:
        q_len = len(q)
        while q_len:
            x, y = q.popleft()

            if x == Dx and y == Dy:
                return dist[x][y]

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < R and 0 <= ny < C and dist[nx][ny] == -1:
                    if graph[nx][ny] == "." or graph[nx][ny] == "D":
                        dist[nx][ny] = dist[x][y] + 1
                        q.append((nx, ny))

            q_len -= 1
        water()  # 주의: 현재 단계를 전부 진행한 이후에 물을 퍼뜨려야 함

    return -1


water()
answer = bfs()

if answer != -1:
    print(answer)
else:
    print("KAKTUS")

"""
- 난이도: 골드4
- 분류: BFS

핵심
- 물을 먼저 퍼뜨리고, 고슴도치를 가능한 곳으로 이동

디버깅
- 문제: 지도의 상태를 매번 큐에 넣는 것은 매우 비효율적
- 해결: 현재 큐에 있는 만큼만 실행 (q_len 활용)
- 참고: https://chldkato.tistory.com/22
"""
