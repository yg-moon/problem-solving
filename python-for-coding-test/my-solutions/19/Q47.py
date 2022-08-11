# BOJ 19236
from collections import defaultdict
from copy import deepcopy

DEAD = 0
SHARK = 100

# 지도상에 각 물고기의 번호만 표시
origin_graph = []

# 물고기 정보: {번호 : [방향, (x좌표, y좌표)]}
# (방향이 0이면 죽은 것)
origin_fish_dic = defaultdict(list)

# 상어 정보: [방향, (x좌표, y좌표)]
origin_shark_info = [0, (0, 0)]

# 먹은 총 물고기 번호를 저장
result = []

# 값 입력
for _ in range(4):
    data = list(map(int, input().split()))
    row = []
    for i in range(8):
        if i % 2 == 0:
            row.append(data[i])
            origin_fish_dic[data[i]].append(data[i + 1])
    origin_graph.append(row)
for i in range(4):
    for j in range(4):
        origin_fish_dic[origin_graph[i][j]].append((i, j))

# dx[1], dy[1]이 '방향 1'에 대응
dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 0, -1, -1, -1, 0, 1, 1, 1]


def move_fish(graph, fish_dic):
    # 모든 물고기에 대해
    for curr_fish in range(1, 17):
        # 물고기가 살아있으면
        dir = fish_dic[curr_fish][0]
        if dir != DEAD:
            x, y = fish_dic[curr_fish][1]
            nx = x + dx[dir]
            ny = y + dy[dir]
            # 이동을 하거나, 이동 불가인게 확인될 때까지
            finished = False
            cnt = 0
            while not finished:
                # 현재 방향으로 이동이 되는지 확인
                # 이동이 되는 경우
                if 0 <= nx < 4 and 0 <= ny < 4 and graph[nx][ny] != SHARK:
                    # 물고기가 있으면 교체
                    next_fish = graph[nx][ny]
                    if next_fish != 0:
                        # 주의: 좌표값만 교체해야지, 방향도 교체하면 안 됨
                        pos1 = fish_dic[curr_fish][1]
                        pos2 = fish_dic[next_fish][1]
                        fish_dic[curr_fish][1] = pos2
                        fish_dic[next_fish][1] = pos1
                        graph[x][y] = next_fish
                    # 빈칸이면 그냥 이동
                    else:
                        fish_dic[curr_fish][1] = (nx, ny)
                        graph[x][y] = 0
                    # 물고기 이동
                    graph[nx][ny] = curr_fish
                    finished = True
                # 이동이 안되는 경우
                else:
                    # 한바퀴 돌았는데도 갈데가 없으면 종료
                    if cnt == 7:
                        finished = True
                    # 될 때까지 방향을 왼쪽으로 틀기
                    else:
                        if dir == 8:
                            dir = 1
                        else:
                            dir += 1
                        nx = x + dx[dir]
                        ny = y + dy[dir]
                        cnt += 1
                        # 주의: 방향 변경사항을 저장해야 함
                        fish_dic[curr_fish][0] = dir


# 초기화: 상어가 (0,0)의 물고기를 먹고 공간에 들어감
origin_shark_info[0] = origin_fish_dic[origin_graph[0][0]][0]  # 상어 방향 변경
origin_shark_info[1] = (0, 0)  # 상어 위치 변경
origin_fish_dic[origin_graph[0][0]][0] = DEAD  # 물고기 사망처리 (방향 0)
origin_fish_sum = origin_graph[0][0]  # 물고기 번호를 합에 추가
origin_graph[0][0] = SHARK  # 상어가 공간에 들어옴


def run(graph, fish_dic, shark_info, fish_sum):
    # 1. 물고기 이동
    move_fish(graph, fish_dic)

    # 2. 상어가 물고기 먹기
    # 가능한 후보들을 파악
    candidates = []
    dir = shark_info[0]
    nx = shark_info[1][0] + dx[dir]
    ny = shark_info[1][1] + dy[dir]
    while 0 <= nx < 4 and 0 <= ny < 4:
        fish = graph[nx][ny]
        if fish != 0:
            candidates.append(fish)
        nx += dx[dir]
        ny += dy[dir]

    # 상어가 이동할 칸이 없으면 시뮬레이션 종료
    if not candidates:
        result.append(fish_sum)
        return
    # DFS 완전탐색
    else:
        # 매 후보들 마다
        for c in candidates:
            # (일단 정보 추출)
            shark_dir = shark_info[0]
            shark_pos = shark_info[1]
            fish_dir = fish_dic[c][0]
            fish_pos = fish_dic[c][1]
            # 후보들을 하나씩 먹고
            graph[shark_pos[0]][shark_pos[1]] = 0
            graph[fish_pos[0]][fish_pos[1]] = SHARK
            shark_info[0] = fish_dir
            shark_info[1] = fish_pos
            fish_dic[c][0] = DEAD
            fish_sum += c
            # 그래프를 복사해서 다음 상황을 돌리고
            run(deepcopy(graph), deepcopy(fish_dic), deepcopy(shark_info), fish_sum)
            # 다시 복구하기
            graph[shark_pos[0]][shark_pos[1]] = SHARK
            graph[fish_pos[0]][fish_pos[1]] = c
            shark_info[0] = shark_dir
            shark_info[1] = shark_pos
            fish_dic[c][0] = fish_dir
            fish_dic[c][1] = fish_pos
            fish_sum -= c


run(
    deepcopy(origin_graph),
    deepcopy(origin_fish_dic),
    deepcopy(origin_shark_info),
    origin_fish_sum,
)

print(max(result))
