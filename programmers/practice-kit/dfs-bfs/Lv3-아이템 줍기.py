# 이동 가능: 바로 옆에 있는 좌표인지
def is_movable(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    if (x1 == x2 and abs(y1 - y2) == 1) or (y1 == y2 and abs(x1 - x2) == 1):
        return True
    else:
        return False


# 테두리 좌표들을 계산
def calc_borders(rectangle):
    borders = []
    not_allowed = set()

    for x1, y1, x2, y2 in rectangle:
        # 모든 좌표를 2배로 계산
        x1 = x1 * 2
        y1 = y1 * 2
        x2 = x2 * 2
        y2 = y2 * 2
        # 다른 사각형 내부에 있는 좌표는 제외
        for i in range(x1 + 1, x2):
            for j in range(y1 + 1, y2):
                not_allowed.add((i, j))

    for x1, y1, x2, y2 in rectangle:
        x1 = x1 * 2
        y1 = y1 * 2
        x2 = x2 * 2
        y2 = y2 * 2
        # 각 사각형의 테두리 좌표를 저장
        rect_border = set()
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if (i, j) not in not_allowed:
                    if i == x1 or i == x2:
                        rect_border.add((i, j))
                    else:
                        if j == y1 or j == y2:
                            rect_border.add((i, j))
        borders.append(rect_border)

    return borders


def solution(rectangle, characterX, characterY, itemX, itemY):
    min_dist = int(1e9)
    visited = set()
    visited.add((characterX * 2, characterY * 2))
    borders = calc_borders(rectangle)

    def dfs(x, y, dist):
        nonlocal min_dist
        if dist >= min_dist:
            return

        if x == itemX * 2 and y == itemY * 2:
            min_dist = min(min_dist, dist)

        for rect in borders:
            for r in rect:
                if r not in visited and is_movable((x, y), r):
                    visited.add(r)
                    dfs(r[0], r[1], dist + 1)
                    visited.remove(r)

    dfs(characterX * 2, characterY * 2, 0)
    return min_dist // 2


"""
요약
- 테두리 좌표의 목록을 만들어둔다.
    - 단, 다른 사각형 내부에 있는 좌표는 제외.
    - 내부: (좌하 x+1, 좌하 y+1) ~ (우상 x-1, 우상 y-1) 사이
- 방문하지 않은 좌표중, 이동 가능한 (x 또는 y 좌표만 1칸 차이나는) 좌표로 이동한다.

DFS
- 파고 들면서 목표지점이 나왔을때 거리 최솟값 갱신.
- 파고 드는 도중, 현재 최솟값을 넘어서면 즉시 중단 (백트래킹)

디버깅: 테두리로만 지나가게 해야 한다.
- 1차: 한칸 띄어있다고 무조건 갈 수 있는게 아니고, 같은 사각형의 점일때만 이동할 수 있다. (허공 이동)
- 2차: 같은 사각형이라고 무조건 갈 수 있는게 아니고, 테두리일 때만 이동할 수 있다. (내부 이동)
- 핵심: 테두리임을 보장할 수 있는 방법이 무엇인가? -> 기존의 크기의 2배로 그려주기!
"""
