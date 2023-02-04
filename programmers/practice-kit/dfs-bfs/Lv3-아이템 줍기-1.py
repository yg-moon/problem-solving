# 이동 가능: 바로 옆에 있는 좌표인지
def is_movable(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    if (x1 == x2 and abs(y1 - y2) == 1) or (y1 == y2 and abs(x1 - x2) == 1):
        return True
    return False


# 테두리 좌표들을 계산
def get_borders(rectangle):
    borders = set()
    not_allowed = set()

    for x1, y1, x2, y2 in rectangle:
        # 핵심: 테두리로만 지나가게 하는 방법 -> 모든 좌표를 2배로 계산 (!)
        x1, y1, x2, y2 = x1 * 2, y1 * 2, x2 * 2, y2 * 2
        # 다른 사각형 내부에 있는 좌표는 제외
        for i in range(x1 + 1, x2):
            for j in range(y1 + 1, y2):
                not_allowed.add((i, j))

    for x1, y1, x2, y2 in rectangle:
        x1, y1, x2, y2 = x1 * 2, y1 * 2, x2 * 2, y2 * 2
        # 테두리 위의 점들을 추가
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if (i, j) not in not_allowed and (i in (x1, x2) or j in (y1, y2)):
                    borders.add((i, j))
    return list(borders)


def solution(rectangle, characterX, characterY, itemX, itemY):
    min_dist = int(1e9)
    visited = set()
    visited.add((characterX * 2, characterY * 2))
    borders = get_borders(rectangle)

    def dfs(x, y, dist):
        # 현재 최솟값을 넘어서면 즉시 중단
        nonlocal min_dist
        if dist >= min_dist:
            return

        # 목표지점이 나왔을때 거리 최솟값 갱신
        if (x, y) == (itemX * 2, itemY * 2):
            min_dist = min(min_dist, dist)

        # 모든 테두리 위의 점에 대해 백트래킹
        for b_pos in borders:
            if b_pos not in visited and is_movable((x, y), b_pos):
                visited.add(b_pos)
                dfs(b_pos[0], b_pos[1], dist + 1)
                visited.remove(b_pos)

    dfs(characterX * 2, characterY * 2, 0)

    return min_dist // 2


"""
요약
- 테두리 좌표의 목록을 만들어둔다.
- DFS로 움직이면서 거리의 최솟값 갱신.
"""
