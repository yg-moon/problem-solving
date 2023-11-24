import sys

sys.setrecursionlimit(10**6)


# 맨해튼 거리
def get_dist(x, y, a, b):
    return abs(x - a) + abs(y - b)


def solution(n, m, x, y, r, c, k):
    dx = [1, 0, 0, -1]
    dy = [0, -1, 1, 0]
    dir = ["d", "l", "r", "u"]
    found = False
    answer = "impossible"

    def dfs(cur_x, cur_y, cnt, path):
        nonlocal answer, found

        # 먼저 도착한 것이 사전순으로 빠름
        if not found:
            dist = get_dist(cur_x, cur_y, r, c)
            # 시간초과 핵심: 가지치기
            if k - cnt - dist < 0:
                return
            if (k - cnt - dist) % 2 == 1:
                return

            if cnt == k:
                if cur_x == r and cur_y == c:
                    found = True
                    answer = "".join(path)
                return

            for i in range(4):
                nx = cur_x + dx[i]
                ny = cur_y + dy[i]
                if 0 < nx <= n and 0 < ny <= m:
                    path.append(dir[i])
                    dfs(nx, ny, cnt + 1, path)
                    path.pop()

    dfs(x, y, 0, [])

    return answer


"""
- 백트래킹 풀이
- 출처: https://allmymight.tistory.com/192

핵심
- 1. 남은 움직임 수가 현재 위치에서 목표지점까지의 거리보다 적으면 가지치기
- 2. 남은 움직임 수에서 현재 위치에서 목표지점까지의 거리를 뺐을때 홀수번 남으면 가지치기
"""
