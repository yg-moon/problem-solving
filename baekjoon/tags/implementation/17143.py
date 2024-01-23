# 낚시왕
R, C, M = map(int, input().split())
graph = [[() for _ in range(C)] for _ in range(R)]
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    graph[r - 1][c - 1] = (s, d, z)

# 1: 위, 2: 아래, 3: 오른쪽, 4: 왼쪽
dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, 1, -1]


# 현재 열에서 땅에 제일 가까운 상어를 한마리 잡음
def catch(col):
    global answer
    for x in range(R):
        if graph[x][col]:
            s, d, z = graph[x][col]
            answer += z
            graph[x][col] = ()
            return


# 반대 방향 구하기
def get_next_dir(dir):
    ret = [0, 2, 1, 4, 3]
    return ret[dir]


# 모든 상어가 움직인 이후의 상태를 리턴
def move():
    ret = [[() for _ in range(C)] for _ in range(R)]

    for x in range(R):
        for y in range(C):
            if graph[x][y]:
                s, d, z = graph[x][y]
                dist = 0
                nx, ny = x, y
                # s만큼 이동
                while dist < s:
                    nx += dx[d]  # 주의: x+dx[d]로 하면 안됨!
                    ny += dy[d]
                    if 0 <= nx < R and 0 <= ny < C:
                        dist += 1
                    else:
                        nx -= dx[d]
                        ny -= dy[d]  # 실수: 여기도 dx로 써버림
                        d = get_next_dir(d)
                # 가장 큰 상어만 남김
                if not ret[nx][ny] or z > ret[nx][ny][2]:
                    ret[nx][ny] = (s, d, z)

    return ret


king_col = -1
answer = 0

while king_col <= C - 2:
    king_col += 1
    catch(king_col)
    graph = move()

print(answer)

"""
- 난이도: 골드1
- 분류: 시뮬레이션
- 소요 시간: 1시간

핵심
- 상어 관리: 2차원 배열 of (s,d,z)
- 상어 이동: 움직인 이후의 그래프를 따로 만들어서 리턴

조건 정리
- 1초마다 낚시왕이 현재 열의 상어를 잡고, 나머지 상어는 이동
- 상어 이동
    - 경계를 넘는 경우 방향을 바꿈
    - 한칸에 두마리가 있으면 가장 큰 상어만 남음
"""
