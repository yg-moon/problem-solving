from collections import deque

keypad = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"], ["*", "0", "#"]]
l_thumb = "*"
r_thumb = "#"
result = ""


def get_pos(target):
    global keypad
    for i in range(4):
        for j in range(3):
            if keypad[i][j] == target:
                return (i, j)
    return (-1, -1)


def get_dist(start, end):
    global keypad
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    start_pos = get_pos(start)
    end_pos = get_pos(end)
    visited = set([start_pos])
    q = deque([[0, start_pos]])
    while q:
        dist, pos = q.popleft()
        if pos == end_pos:
            return dist
        for i in range(4):
            nx = pos[0] + dx[i]
            ny = pos[1] + dy[i]
            if 0 <= nx <= 3 and 0 <= ny <= 2 and (nx, ny) not in visited:
                q.append((dist + 1, (nx, ny)))
                visited.add((nx, ny))
    return -1


def move_l(num):
    global result, l_thumb
    result += "L"
    l_thumb = str(num)


def move_r(num):
    global result, r_thumb
    result += "R"
    r_thumb = str(num)


def solution(numbers, hand):
    for num in numbers:
        if num in [1, 4, 7]:
            move_l(num)
        elif num in [3, 6, 9]:
            move_r(num)
        else:
            l_dist = get_dist(l_thumb, str(num))
            r_dist = get_dist(r_thumb, str(num))
            if l_dist < r_dist:
                move_l(num)
            elif l_dist > r_dist:
                move_r(num)
            else:
                if hand == "left":
                    move_l(num)
                else:
                    move_r(num)

    return result


"""
- 분류: 구현
- 소요 시간: 40분

- BFS 풀이
"""
