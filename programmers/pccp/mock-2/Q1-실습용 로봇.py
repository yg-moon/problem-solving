def solution(command):
    # 북동남서
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    x, y = 0, 0
    dir = 0

    for c in command:
        if c == "R":
            dir = (dir + 1) % 4
        elif c == "L":
            dir = (dir - 1) % 4
        elif c == "G":
            x += dx[dir]
            y += dy[dir]
        elif c == "B":
            x -= dx[dir]
            y -= dy[dir]

    return [x, y]


"""
- 전체 문제 읽기: 10:35-10:40 (5분)

- 분류: 구현, 그래프
- 시간: 10:40-10:45 (5분)
"""
