from collections import deque

R, C = map(int, input().split())
graph = [list(input()) for _ in range(R)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

q = deque()
dist = [[0] * C for _ in range(R)]

# 시작점, 도착점, 물의 위치
for x in range(R):
    for y in range(C):
        if graph[x][y] == "S":
            q.appendleft((x, y))  # 주의: 고슴도치가 먼저 들어가야 함
        elif graph[x][y] == "D":
            Dx, Dy = x, y
        elif graph[x][y] == "*":
            q.append((x, y))


# 큐 1개만 사용하기: 고슴도치를 먼저 넣고, 이어서 물의 위치를 넣기
def bfs():
    while q:
        x, y = q.popleft()

        if graph[Dx][Dy] == "S":
            return dist[Dx][Dy]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < R and 0 <= ny < C):
                continue
            # 고슴도치
            if graph[x][y] == "S" and (graph[nx][ny] == "." or graph[nx][ny] == "D"):
                dist[nx][ny] = dist[x][y] + 1
                graph[nx][ny] = "S"
                q.append((nx, ny))
            # 물
            elif graph[x][y] == "*" and (graph[nx][ny] == "." or graph[nx][ny] == "S"):
                graph[nx][ny] = "*"
                q.append((nx, ny))

    return -1


answer = bfs()

if answer != -1:
    print(answer)
else:
    print("KAKTUS")

"""
큐를 1개만 사용하는 풀이
- 방법: 고슴도치 위치를 먼저 넣고, 물의 위치를 넣으면 됨
- 단점: 디버깅시 과정 확인이 어려움
- 참고: https://wookcode.tistory.com/167
"""
