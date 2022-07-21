def check(place):
    for irow, row in enumerate(place):
        for icol, cell in enumerate(row):
            # 현재 좌표가 P인 경우에 대해서만 탐색
            if cell != "P":
                continue
            # 1칸 아래에 있는 경우
            if irow != 4 and place[irow + 1][icol] == "P":
                return 0
            # 1칸 오른쪽에 있는 경우
            if icol != 4 and place[irow][icol + 1] == "P":
                return 0
            # 2칸 아래 있는데 중간에 X가 없는 경우
            if (
                irow < 3
                and place[irow + 2][icol] == "P"
                and place[irow + 1][icol] != "X"
            ):
                return 0
            # 2칸 오른쪽에 있는데 중간에 X가 없는 경우
            if (
                icol < 3
                and place[irow][icol + 2] == "P"
                and place[irow][icol + 1] != "X"
            ):
                return 0
            # 대각 오른쪽아래 있는데 나머지 X가 아닐 경우
            if (
                irow != 4
                and icol != 4
                and place[irow + 1][icol + 1] == "P"
                and (place[irow + 1][icol] != "X" or place[irow][icol + 1] != "X")
            ):
                return 0
            # 대각 왼쪽아래 있는데 나머지가 X가 아닐 경우
            if (
                irow != 4
                and icol != 0
                and place[irow + 1][icol - 1] == "P"
                and (place[irow + 1][icol] != "X" or place[irow][icol - 1] != "X")
            ):
                return 0
    return 1


def solution(places):
    return [check(place) for place in places]
