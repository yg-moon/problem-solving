# 마법사 상어와 비바리기
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
moves = [list(map(int, input().split())) for _ in range(M)]

# 8방향 (1-idx)
dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]

# 대각선 방향
dx2 = [-1, -1, 1, 1]
dy2 = [-1, 1, -1, 1]

# 구름 위치
clouds = [(N - 1, 0), (N - 1, 1), (N - 2, 0), (N - 2, 1)]

# M번의 이동
for dir, dist in moves:
    # 구름 이동
    moved_clouds = []
    for x, y in clouds:
        nx = (x + dx[dir] * dist) % N  # 주의: abs를 쓰면 안됨
        ny = (y + dy[dir] * dist) % N  # 주의: y도 N임
        moved_clouds.append((nx, ny))

    # 비 내림
    for x, y in moved_clouds:
        graph[x][y] += 1

    # 물 복사
    for x, y in moved_clouds:
        for i in range(4):
            nx = x + dx2[i]
            ny = y + dy2[i]
            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] >= 1:
                graph[x][y] += 1

    # 새로운 구름 생성
    new_clouds = []
    for x in range(N):
        for y in range(N):
            if graph[x][y] >= 2 and (x, y) not in moved_clouds:
                graph[x][y] -= 2
                new_clouds.append((x, y))

    clouds = new_clouds

answer = 0
for x in range(N):
    for y in range(N):
        answer += graph[x][y]
print(answer)

"""
- 난이도: 골드5
- 분류: 시뮬레이션
- 소요 시간: 50분

요약
- 시키는대로 구현하는 문제
- 핵심: 구름의 상태를 clouds, moved_clouds, new_clouds로 구분

조건 정리
- 1행과 N행, 1열과 N열은 연결되어 있음
- 처음엔 (N, 1), (N, 2), (N-1, 1), (N-1, 2)에 비구름이 생김
- 구름 이동 -> 비내림 -> 물복사
- 바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고, 물의 양이 2 줄어든다.
    - 이때 구름이 생기는 칸은 3에서 구름이 사라진 칸이 아니어야 한다.
"""
