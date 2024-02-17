from collections import deque, defaultdict


def solution(land):
    N = len(land)
    M = len(land[0])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    dic = defaultdict(int)  # {섬 번호: 석유량}
    visited = [[False] * M for _ in range(N)]
    land_num = 2

    # 현재 덩어리에 번호를 매기고, 석유량을 기록
    def bfs(sx, sy, num):
        q = deque()
        q.append((sx, sy))
        cnt = 0

        while q:
            x, y = q.popleft()
            land[x][y] = num
            cnt += 1

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if (
                    0 <= nx < N
                    and 0 <= ny < M
                    and land[nx][ny] == 1
                    and not visited[nx][ny]
                ):
                    q.append((nx, ny))
                    visited[nx][ny] = True

        dic[num] = cnt

    # 모든 덩어리를 찾고, 석유량을 기록
    for i in range(N):
        for j in range(M):
            if land[i][j] == 1 and not visited[i][j]:
                bfs(i, j, land_num)
                land_num += 1

    # 모든 열에 시추관을 뚫어보기
    max_oil = 0
    for j in range(M):
        seen = set()
        cur_oil = 0
        for i in range(N):
            num = land[i][j]
            if num != 0 and num not in seen:
                cur_oil += dic[num]
                seen.add(num)
        max_oil = max(max_oil, cur_oil)

    return max_oil


"""
- 난이도: Lv2
- 분류: DFS/BFS
- 소요 시간: 15분

요약
- BFS로 섬 만들기
- dict로 {섬 번호: 석유량} 만들기
- 세로로 뚫으면서 최대 석유량 뽑는 경우 찾기
"""
