def solution(places):
    answer = []

    def check(list_p, list_x):
        for pair1 in list_p:
            for pair2 in list_p:
                mht = abs(pair1[0] - pair2[0]) + abs(pair1[1] - pair2[1])
                if mht <= 2 and mht != 0:
                    # horizontal
                    if pair1[0] == pair2[0]:
                        # right next to each other
                        if abs(pair1[1] - pair2[1]) <= 1:
                            answer.append(0)
                            return
                        # pair1 is left
                        if pair1[1] < pair2[1]:
                            if (pair1[0], pair1[1] + 1) not in list_x:
                                answer.append(0)
                                return
                        # pair1 is right
                        else:
                            if (pair1[0], pair1[1] - 1) not in list_x:
                                answer.append(0)
                                return
                    # vertical
                    elif pair1[1] == pair2[1]:
                        # right next to each other
                        if abs(pair1[0] - pair2[0]) <= 1:
                            answer.append(0)
                            return
                        # pair1 is over
                        if pair1[0] > pair2[0]:
                            if (pair1[0] - 1, pair1[1]) not in list_x:
                                answer.append(0)
                                return
                        # pair1 is below
                        else:
                            if (pair1[0] + 1, pair1[1]) not in list_x:
                                answer.append(0)
                                return
                    # diagonal
                    else:
                        # case1: pair1 is upper left
                        if pair1[0] < pair2[0] and pair1[1] < pair2[1]:
                            if (pair1[0], pair1[1] + 1) not in list_x or \
                                (pair1[0] + 1, pair1[1]) not in list_x:
                                answer.append(0)
                                return
                        # case2: pair1 is upper right
                        elif pair1[0] < pair2[0] and pair1[1] > pair2[1]:
                            if (pair1[0], pair1[1] - 1) not in list_x or \
                                (pair1[0] + 1, pair1[1]) not in list_x:
                                answer.append(0)
                                return
                        # case3: pair1 is lower left
                        elif pair1[0] > pair2[0] and pair1[1] > pair2[1]:
                            if (pair1[0] - 1, pair1[1]) not in list_x or \
                                (pair1[0], pair1[1] - 1) not in list_x:
                                answer.append(0)
                                return
                        # case4: pair1 is lower right
                        elif pair1[0] > pair2[0] and pair1[1] < pair2[1]:
                            if (pair1[0] - 1, pair1[1]) not in list_x or \
                                (pair1[0], pair1[1] + 1,) not in list_x:
                                answer.append(0)
                                return
        answer.append(1)
        return

    for place in places:
        list_p = []
        list_x = []
        for i in range(5):
            for j in range(5):
                if place[i][j] == "P":
                    list_p.append((i, j))
                if place[i][j] == "X":
                    list_x.append((i, j))
        check(list_p, list_x)

    return answer
