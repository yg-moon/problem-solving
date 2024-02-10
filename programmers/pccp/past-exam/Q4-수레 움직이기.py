def solution(maze):
    INF = int(1e9)
    N = len(maze)
    M = len(maze[0])
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    r_visited = [[False] * M for _ in range(N)]
    b_visited = [[False] * M for _ in range(N)]
    answer = INF

    # 시작지점 및 도착지점 추출
    for i in range(N):
        for j in range(M):
            if maze[i][j] == 1:
                Rx, Ry = i, j
                r_visited[Rx][Ry] = True
            elif maze[i][j] == 2:
                Bx, By = i, j
                b_visited[Bx][By] = True
            elif maze[i][j] == 3:
                target_rx, target_ry = i, j
            elif maze[i][j] == 4:
                target_bx, target_by = i, j

    def dfs(rx, ry, bx, by, r_moved, r_done, b_moved, b_done, cnt):
        nonlocal answer

        # 가지치기: 이미 최소횟수를 넘었으면 조기종료
        if cnt >= answer:
            return

        # 정답을 찾은 경우
        if r_done and b_done:
            answer = min(answer, cnt + 1)
            return

        # 다음 턴으로 넘어가기
        if r_moved and b_moved or r_done and b_moved or b_done and r_moved:
            r_moved = False
            b_moved = False
            cnt += 1

        # 빨강 움직이기
        if not r_done and not r_moved:
            for i in range(4):
                nrx = rx + dx[i]
                nry = ry + dy[i]
                if (
                    0 <= nrx < N
                    and 0 <= nry < M
                    and not r_visited[nrx][nry]
                    and (nrx, nry) != (bx, by)
                    and maze[nrx][nry] != 5
                ):
                    is_done = False
                    if (nrx, nry) == (target_rx, target_ry):
                        is_done = True
                    r_visited[nrx][nry] = True
                    dfs(nrx, nry, bx, by, True, is_done, b_moved, b_done, cnt)
                    r_visited[nrx][nry] = False

        # 파랑 움직이기
        if not b_done and not b_moved:
            for i in range(4):
                nbx = bx + dx[i]
                nby = by + dy[i]
                if (
                    0 <= nbx < N
                    and 0 <= nby < M
                    and not b_visited[nbx][nby]
                    and (nbx, nby) != (rx, ry)
                    and maze[nbx][nby] != 5
                ):
                    is_done = False
                    if (nbx, nby) == (target_bx, target_by):
                        is_done = True
                    b_visited[nbx][nby] = True
                    dfs(rx, ry, nbx, nby, r_moved, r_done, True, is_done, cnt)
                    b_visited[nbx][nby] = False

    dfs(Rx, Ry, Bx, By, False, False, False, False, 0)

    if answer == INF:
        return 0
    else:
        return answer


"""
- 난이도: Lv3
- 분류: 백트래킹, 시뮬레이션
- 소요 시간: 45분

요약
- 목표는 1->3, 2->4
- 차례를 구분하여 빨강, 파랑을 이동: moved와 done 여부를 확인

디버깅
1. 틀렸습니다
    - 상대방이 방문했던 칸으로 움직이면 안된다는 조건은 없음
2. 시간초과
    - 최대 4x4 인데도 가지치기 안하니까 터지네
"""
