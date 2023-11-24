def solution(n, m, x, y, r, c, k):
    def can_go(x, y, k):
        return abs(r - x) + abs(c - y) <= k

    def out_of_range(x, y):
        return x < 0 or y < 0 or x >= n or y >= n

    x = x - 1
    y = y - 1
    r = r - 1
    c = c - 1
    dx = [1, 0, 0, -1]
    dy = [0, -1, 1, 0]
    cur_x = x
    cur_y = y
    answer = ""

    while k != 0:
        moved = False

        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            if not out_of_range(nx, ny) and can_go(nx, ny, k - 1):
                k -= 1
                cur_x = nx
                cur_y = ny
                moved = True
                answer += "dlru"[i]
                break

        if not moved:
            return "impossible"

    return answer


"""
- 그리디 풀이
- 출처: https://ps.mjstudio.net/kakao-coding-test#6-미로-탈출-명령어-lv3-152-min-ac

핵심
- 각 순간에 dlru 순으로 가능/불가능 여부만 판단해서 최적으로 계속 진행하면 됨
- 불가능 판단 여부는 보드 밖으로 나가거나, 거기로 이동시 남은 k-1번의 횟수안에 도착점에 못가는 경우
"""
