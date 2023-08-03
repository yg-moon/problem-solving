num_pos_dict = {
    0: (3, 1),
    1: (0, 0),
    2: (0, 1),
    3: (0, 2),
    4: (1, 0),
    5: (1, 1),
    6: (1, 2),
    7: (2, 0),
    8: (2, 1),
    9: (2, 2),
    "*": (3, 0),
    "#": (3, 2),
}
l_thumb = num_pos_dict["*"]
r_thumb = num_pos_dict["#"]
result = ""


def get_dist(cur_pos, next_pos):
    return abs(cur_pos[0] - next_pos[0]) + abs(cur_pos[1] - next_pos[1])


def move_l(num):
    global result, l_thumb
    result += "L"
    l_thumb = num_pos_dict[num]


def move_r(num):
    global result, r_thumb
    result += "R"
    r_thumb = num_pos_dict[num]


def solution(numbers, hand):
    for num in numbers:
        if num in [1, 4, 7]:
            move_l(num)
        elif num in [3, 6, 9]:
            move_r(num)
        else:
            l_dist = get_dist(l_thumb, num_pos_dict[num])
            r_dist = get_dist(r_thumb, num_pos_dict[num])
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
