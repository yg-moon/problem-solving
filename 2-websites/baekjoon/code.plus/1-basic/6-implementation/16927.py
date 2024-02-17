# 배열 돌리기 2
N, M, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # D R U L


def rotate(arr):
    r = len(arr)
    c = len(arr[0])
    ret = [[0] * c for _ in range(r)]
    visited = [[False] * c for _ in range(r)]

    # 시작점: i == j 중에, 행과 열의 절반을 넘지 않는 좌표까지.
    starts = [(0, 0)]
    max_start = min(r // 2 - 1, c // 2 - 1)
    if max_start >= 1:
        for i in range(1, max_start + 1):
            starts.append((i, i))

    for start in starts:
        x, y = start
        cur_dir = 0
        # 바깥쪽부터 한줄씩 떼어내기
        shell = []  # [[(좌표 정보1), 값1], ...]
        while True:
            nx, ny = x + dirs[cur_dir][0], y + dirs[cur_dir][1]
            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny]:
                shell.append([(x, y), arr[x][y]])
                ret[nx][ny] = arr[x][y]
                visited[nx][ny] = True
                x, y = nx, ny
            else:
                cur_dir += 1
                if cur_dir == 4:
                    break
        # R번 밀어낸 이후의 상태를 계산
        values_after_rotation = [0] * len(shell)
        for i in range(len(shell)):
            values_after_rotation[(i + R) % len(shell)] = shell[i][1]
        # 다시 원래 자리에 붙이기
        for i in range(len(shell)):
            x, y = shell[i][0]
            ret[x][y] = values_after_rotation[i]

    return ret


arr = rotate(arr)

for row in arr:
    print(*row)

"""
- 요약
    - 배열 돌리기1 과의 차이점: 회전 최대 횟수가 10억으로 크게 늘어났다.
    - 매번 직접 돌리는게 아니라, 다 돌렸을 때의 결과를 한번에 계산해야 한다.
- 구현
    - 바깥쪽부터 한줄씩 떼어내서, R번 밀어낸 이후의 상태를 계산하고, 다시 원래 자리에 붙이기.
        - 매번 한줄씩 떼어내서 일자로 늘어놓기.
        - 임시 배열의 `(현재위치 + R) % 한줄 길이` 위치에 현재위치의 배열값을 넣는다.
        - 2차원 배열에서의 원래 위치에 임시 배열 값을 넣으면 끝.
            - 이렇게 하기 위해서는 한줄씩 떼어낼 때 원래 위치까지 가져와야 한다.
"""
