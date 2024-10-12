# 청소년 상어
import copy

directions = [
    (-1, 0),  # ↑ 방향 0
    (-1, -1),  # ↖ 방향 1
    (0, -1),  # ← 방향 2
    (1, -1),  # ↙ 방향 3
    (1, 0),  # ↓ 방향 4
    (1, 1),  # ↘ 방향 5
    (0, 1),  # → 방향 6
    (-1, 1),  # ↗ 방향 7
]

# 초기 설정
grid = []
fish_info = dict()  # 물고기 정보: 번호를 키로 사용

for i in range(4):
    data = list(map(int, input().split()))
    row = []
    for j in range(4):
        fish_num = data[2 * j]
        fish_dir = data[2 * j + 1] - 1  # 방향을 0부터 시작하도록 조정
        row.append(fish_num)
        fish_info[fish_num] = [i, j, fish_dir]
    grid.append(row)

# 상어의 초기 위치와 방향
shark_x, shark_y = 0, 0
shark_dir = fish_info[grid[0][0]][2]
total = grid[0][0]
del fish_info[grid[0][0]]
grid[0][0] = -1  # 상어의 위치를 -1로 표시


def move_all_fish(grid, fish_info):
    for fish_num in range(1, 17):
        if fish_num in fish_info:
            x, y, dir = fish_info[fish_num]
            for i in range(8):
                ndir = (dir + i) % 8
                dx, dy = directions[ndir]
                nx, ny = x + dx, y + dy
                if 0 <= nx < 4 and 0 <= ny < 4 and grid[nx][ny] != -1:
                    # 이동 가능
                    if grid[nx][ny] == 0:
                        grid[x][y], grid[nx][ny] = grid[nx][ny], grid[x][y]
                        fish_info[fish_num] = [nx, ny, ndir]
                    else:
                        other_fish = grid[nx][ny]
                        grid[x][y], grid[nx][ny] = grid[nx][ny], grid[x][y]
                        fish_info[fish_num] = [nx, ny, ndir]
                        fish_info[other_fish][0], fish_info[other_fish][1] = x, y
                    break


def dfs(grid, fish_info, shark_x, shark_y, shark_dir, total):
    max_total = total
    grid = copy.deepcopy(grid)
    fish_info = copy.deepcopy(fish_info)
    move_all_fish(grid, fish_info)
    for step in range(1, 4):
        nx = shark_x + directions[shark_dir][0] * step
        ny = shark_y + directions[shark_dir][1] * step
        if 0 <= nx < 4 and 0 <= ny < 4:
            if grid[nx][ny] > 0:
                fish_num = grid[nx][ny]
                ndir = fish_info[fish_num][2]
                grid[shark_x][shark_y] = 0
                grid[nx][ny] = -1
                del fish_info[fish_num]
                result = dfs(grid, fish_info, nx, ny, ndir, total + fish_num)
                max_total = max(max_total, result)
                grid[shark_x][shark_y] = -1
                grid[nx][ny] = fish_num
                fish_info[fish_num] = [nx, ny, ndir]
        else:
            break
    return max_total


result = dfs(grid, fish_info, shark_x, shark_y, shark_dir, total)
print(result)

"""
문제 핵심 조건:
- 4x4 공간에서 물고기와 상어의 이동을 시뮬레이션.
- 물고기는 번호 순서대로 이동하며, 이동 가능한 방향을 찾기 위해 최대 8번 회전.
- 상어는 자신의 방향으로 최대 3칸 이동 가능하며, 물고기가 있는 칸으로만 이동.
- 상어가 먹을 수 있는 물고기 번호의 합의 최댓값을 구하는 문제.

구현 흐름:
1. 초기 상태에서 상어가 (0,0)의 물고기를 먹고 시작하며, 물고기의 방향을 갖는다.
2. 재귀 함수를 통해 모든 가능한 상어의 이동 경로를 탐색(DFS).
   - 각 재귀 단계에서 물고기들을 이동시키고, 상어의 다음 이동을 결정.
   - 상어의 가능한 이동 위치마다 재귀 호출하여 최대 합을 갱신.
3. 물고기의 이동과 상어의 이동 시 상태를 복사하여 이전 상태에 영향이 없도록 함.
4. 모든 가능한 경우를 탐색하여 상어가 먹을 수 있는 물고기 번호의 합의 최댓값을 출력.
"""
