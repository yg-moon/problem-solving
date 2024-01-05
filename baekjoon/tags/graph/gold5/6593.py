# 상범 빌딩
from collections import deque

dz = [0, 0, 0, 0, 1, -1]
dx = [-1, 0, 1, 0, 0, 0]
dy = [0, -1, 0, 1, 0, 0]


def bfs(sz, sx, sy):  # 주의: 순서를 헷갈리지 않게 확실하게 인자로 작성하기
    q = deque()
    q.append((sz, sx, sy, 0))
    visited = [[[False] * C for _ in range(R)] for _ in range(L)]
    visited[sz][sx][sy] = True
    ret = -1

    while q:
        z, x, y, time = q.popleft()

        if graph[z][x][y] == "E":
            ret = time
            break

        for i in range(6):
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]
            if (
                0 <= nz < L
                and 0 <= nx < R
                and 0 <= ny < C
                and not visited[nz][nx][ny]
                and graph[nz][nx][ny] != "#"
            ):
                q.append((nz, nx, ny, time + 1))
                visited[nz][nx][ny] = True

    return ret


while True:
    L, R, C = map(int, input().split())

    if L == 0 and R == 0 and C == 0:
        break

    graph = [[list(input()) for _ in range(R + 1)] for _ in range(L)]

    for i in range(L):
        for j in range(R):
            for k in range(C):
                if graph[i][j][k] == "S":
                    answer = bfs(i, j, k)
                    break

    if answer != -1:
        print(f"Escaped in {answer} minute(s).")
    else:
        print("Trapped!")

"""
- 난이도: 골드5
- 분류: BFS
- 소요 시간: 50분 (풀이 20분, 디버깅 30분)

- 기본적인 3차원 BFS

디버깅: 인덱스 에러
- 원인: 시작점을 z,x,y 기준으로 탐색해놓고 다시 x,y,z 순서로 착각해서 잘못 작업함
- 해결: 함수 인자에 명확하게 표시
"""
