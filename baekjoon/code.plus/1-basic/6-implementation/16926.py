# 배열 돌리기 1
N, M, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # D R U L


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
        curr_dir = 0
        stop = False
        while not stop:
            nx, ny = x + dir[curr_dir][0], y + dir[curr_dir][1]
            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny]:
                ret[nx][ny] = arr[x][y]
                visited[nx][ny] = True
                x, y = nx, ny
            else:
                curr_dir += 1
                if curr_dir == 4:
                    stop = True

    return ret


for _ in range(R):
    arr = rotate(arr)

for row in arr:
    print(*row)

"""
- 요약: 매번 왼쪽 위를 시작점으로 잡고, 바깥쪽부터 한줄씩 회전시키기.
- 구현
    - 시작점은 어디까지 잡아야 하는가?
        - i == j 중에, 행과 열의 절반을 넘지 않는 위치까지.
    - 매번 어디까지 움직여야 하는가?
        - visited를 통해 관리.
- 로직
    - 가능한 모든 시작점에 대해
        - 매번 시작점에서 출발. 이때 항상 처음 방향(아래쪽)을 보고 시작.
        - 현재 방향을 보고, 방문하지 않았고 범위를 벗어나지 않으면 그 위치에 값을 넣어주고 방문처리.
            - 방문했거나 범위를 벗어났다면 다음 방향으로 바꿔주기.
        - 현재 방향이 마지막 방향이라면 지금 시작점에 대해서는 종료.
"""
