import itertools

# 테두리 위의 점인지 확인
def is_movable(cur_x, cur_y, next_x, next_y, rectangle):
    # 두 좌표의 중간 지점을 확인 기준으로 사용
    x = (cur_x + next_x) / 2  # 주의: // 로 하면 안됨!
    y = (cur_y + next_y) / 2

    is_on_any_border = any(
        (x in (x1, x2) and y1 <= y <= y2) or (y in (y1, y2) and x1 <= x <= x2)
        for x1, y1, x2, y2 in rectangle
    )
    is_inside_any_rect = any(
        x1 < x < x2 and y1 < y < y2 for x1, y1, x2, y2 in rectangle
    )

    return is_on_any_border and not is_inside_any_rect


def solution(rectangle, characterX, characterY, itemX, itemY):
    cur_pos = (characterX, characterY)
    prev_pos = None

    for dist in itertools.count():
        # 한바퀴 돌았는지 확인
        if cur_pos == (characterX, characterY) and prev_pos:
            perimeter = dist
            break
        # 목적지에 도착한 경우
        elif cur_pos == (itemX, itemY):
            dist_to_item = dist
        # 다음 칸으로 이동
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            next_pos = (cur_pos[0] + dx, cur_pos[1] + dy)
            if next_pos != prev_pos and is_movable(*cur_pos, *next_pos, rectangle):
                prev_pos, cur_pos = cur_pos, next_pos
                break

    return min(dist_to_item, perimeter - dist_to_item)


"""
- 출처: http://www.teferi.net/ps/problems/programmers/87694
- 테두리를 따라서 한칸씩 이동하며 한바퀴를 돌면서, 전체 둘레 및 아이템까지의 거리를 잰다.
"""
