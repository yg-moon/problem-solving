# 드래곤 커브
N = int(input())
dragons = [list(map(int, input().split())) for _ in range(N)]
graph = [[0] * 101 for _ in range(101)]
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for x, y, d, g in dragons:
    # 각 커브의 시작점
    graph[x][y] = 1

    # 모든 선분의 방향 구하기
    dirs = [d]
    for _ in range(g):
        for i in reversed(range(len(dirs))):
            dirs.append((dirs[i] + 1) % 4)

    # 드래곤 커브 그리기
    for dir in dirs:
        nx = x + dx[dir]
        ny = y + dy[dir]
        graph[nx][ny] = 1
        x, y = nx, ny

# 모든 꼭짓점이 드래곤 커브의 일부인 정사각형 개수 구하기
answer = 0
for i in range(100):
    for j in range(100):
        if (
            graph[i][j] == 1
            and graph[i + 1][j] == 1
            and graph[i][j + 1] == 1
            and graph[i + 1][j + 1] == 1
        ):
            answer += 1
print(answer)

"""
- 요약: 각 선분들의 방향이 변화하는 패턴을 찾아서, 모든 선분의 방향 정보를 구하여 커브를 그린다.
- 구현
    - 핵심: 각 세대가 진행될때마다, 이전 세대의 정보를 뒤집어 1을 더해주면 된다.
    - ex.
        - 0세대 : 0
        - 1세대 : 0 - 1
        - 2세대 : 0 1 - 2 1
        - 3세대 : 0 1 2 1 - 2 3 2 1
        - 4세대 : 0 1 2 1 2 3 2 1 - 2 3 0 3 2 3 2 1
- 출처
    - https://kyun2da.github.io/2021/04/06/dragonCurve/
    - https://tmdrl5779.tistory.com/146
"""
