# BOJ 19237
from collections import defaultdict

N, M, k = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

# 초기방향 임시저장
init_dir = defaultdict(int)
data = list(map(int, input().split()))
for i in range(M):
    init_dir[i + 1] = data[i]

# 우선순위 정보
priority = defaultdict(list)
for i in range(M):
    priority[i + 1].append([0])
    for _ in range(4):
        priority[i + 1].append(list(map(int, input().split())))

# 그래프 재구성: 칸 마다 [상어 번호, 상어 방향, 냄새 번호, 냄새 남은 시간]
for x in range(N):
    for y in range(N):
        if graph[x][y] == 0:
            graph[x][y] = [0, 0, 0, 0]
        else:
            shark_id = graph[x][y]
            shark_dir = init_dir[shark_id]
            smell_id = shark_id
            smell_time = k
            graph[x][y] = [shark_id, shark_dir, smell_id, smell_time]

# idx 1,2,3,4 순으로 상하좌우
dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]

shark_cnt = M
time = 0

# k를 상수로 사용
def get_k():
    return k


while True:
    new_graph = [[[0 for _ in range(4)] for _ in range(N)] for _ in range(N)]
    seen = set()

    # 모든 상어 이동
    for x in range(N):
        for y in range(N):
            info = graph[x][y]
            # 상어가 없으면, 냄새만 줄이기 (냄새도 없으면 패스)
            if info[0] == 0:
                # 주의: 이번 반복에 들어온 상어나 냄새가 없을때만 실행
                if new_graph[x][y][2] == 0:
                    # 냄새가 있는 경우
                    if info[2] != 0:
                        # 남은 냄새가 1인 경우
                        if info[3] == 1:
                            new_graph[x][y] = [0, 0, 0, 0]
                        else:
                            new_graph[x][y] = [0, 0, info[2], info[3] - 1]
            # 상어가 있으면
            else:
                # 이미 움직인 상어라면, 패스
                if info[0] in seen:
                    continue

                # 빈칸을 찾아서, 우선순위 4방향대로 다음 칸 결정
                has_space = False
                next_dir = 0
                for i in range(4):
                    next_dir = priority[info[0]][info[1]][i]
                    nx = x + dx[next_dir]
                    ny = y + dy[next_dir]
                    if 0 <= nx < N and 0 <= ny < N and graph[nx][ny][2] == 0:
                        has_space = True
                        break

                # 빈칸이 없다면, 내 냄새를 찾아서 우선순위 4방향대로 다음 칸 결정
                if not has_space:
                    for i in range(4):
                        next_dir = priority[info[0]][info[1]][i]
                        nx = x + dx[next_dir]
                        ny = y + dy[next_dir]
                        if 0 <= nx < N and 0 <= ny < N and graph[nx][ny][2] == info[0]:
                            break

                # 상어 움직이기
                # 1. 현재 위치에 내 냄새 남기기
                new_graph[x][y] = [0, 0, info[2], get_k() - 1]

                # 2. 다음 위치로 이동하기
                new_info = new_graph[nx][ny]
                # 다음 칸이 비었거나, 내가 더 작을 경우: 현재 상어 이동
                # (즉, 이미 상어가 있다면 더 낮은 것이 살아남음)
                if new_info[0] == 0 or new_info[0] > info[0]:
                    new_graph[nx][ny] = [info[0], next_dir, info[0], get_k()]
                # 경쟁이 있었을 경우: 상어 마리수 -1
                if new_info[0] != 0:
                    shark_cnt -= 1

                # 3. 움직인 상어는 기록에 추가
                seen.add(info[0])

    # 소요 시간 +1
    time += 1

    # 조건에 따라 종료
    if shark_cnt == 1 or time >= 1000:
        break

    # 그래프 복사
    graph = new_graph


# 결과 출력
if shark_cnt >= 2 and time >= 1000:
    print(-1)
else:
    print(time)
