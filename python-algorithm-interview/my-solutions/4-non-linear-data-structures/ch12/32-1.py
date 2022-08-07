# LeetCode 200
from typing import List

LAND = "1"
VISITED = "2"


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            # 범위를 벗어나거나, 땅이 아니면 종료
            if not (
                0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == LAND
            ):
                return
            # 방문한 곳을 표시
            grid[i][j] = VISITED
            # 상하좌우 재귀 탐색
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        # 그래프 전체를 돌며 LAND를 만나면 DFS 수행
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == LAND:
                    dfs(i, j)
                    # 연결된 모든 육지 탐색 후 카운트 1 증가
                    cnt += 1
        return cnt
