# 망함.
def solution(n, build_frame):
    pillars = []
    plates = []

    for x, y, a, b in build_frame:
        # 설치
        if b == 1:
            # 기둥 설치
            if a == 0:
                if (
                    y == 0
                    or (x, y - 1) in pillars
                    or (x, y) in plates
                    or (x - 1, y) in plates
                ):
                    pillars.append((x, y))
            # 보 설치
            elif a == 1:
                if (
                    (x, y - 1) in pillars
                    or (x + 1, y - 1) in pillars
                    or ((x - 1, y) in plates and (x + 1, y) in plates)
                ):
                    plates.append((x, y))
        # 삭제
        elif b == 0:
            # 기둥 삭제
            if a == 0:
                # 위에 기둥이 없어야 함
                if (x, y + 1) not in pillars:
                    curr_valid = True
                    left_valid = True
                    # 위에 보가 있다면, 받치는 기둥이 있거나, 연결된 보가 있어야 함
                    curr_plate = (x, y + 1)
                    left_plate = (x - 1, y - 1)
                    if curr_plate in plates:
                        if (curr_plate[0] + 1, curr_plate[1] - 1) not in pillars and (
                            curr_plate[0] + 1,
                            curr_plate[1],
                        ) not in plates:
                            curr_valid = False
                    if left_plate in plates:
                        if (left_plate[0], left_plate[1] - 1) not in pillars and (
                            left_plate[0] - 2,
                            left_plate[1],
                        ) not in plates:
                            left_valid = False
                    if curr_valid and left_valid:
                        pillars.remove((x, y))
            # 보 삭제
            elif a == 1:
                case1 = True
                case2 = True
                # Case1: 삭제할 보 위에 기둥이 있는데, 밑에 받침 기둥도 없고, 옆에 받침 보도 없을 때.
                if (x, y) in pillars:
                    if (x, y - 1) not in pillars and (x - 1, y) not in plates:
                        case1 = False
                if (x + 1, y) in pillars:
                    if (x + 1, y - 1) not in pillars and (x + 1, y) not in plates:
                        case1 = False
                # Case2: 삭제할 보 양 옆으로 보가 또 있는데, 밑에 받침 기둥도 없고, 양옆보 중 하나라도 기둥이 없을 때.
                if (x - 1, y) in plates and (x + 1, y) in plates:
                    if (x, y - 1) not in pillars and (x + 1, y - 1) not in pillars:
                        if (x - 1, y - 1) not in pillars or (x + 2, y - 1) not in pillars:
                            case2 = False
                if case1 and case2:
                    plates.remove((x, y))

    # 정답 출력
    answer = []
    for p in pillars:
        answer.append([p[0], p[1], 0])
    for p in plates:
        answer.append([p[0], p[1], 1])
    # 마지막 리턴값은 x, y, a 기준으로 정렬
    answer.sort()

    return answer
