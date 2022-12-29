# ACM 호텔
T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())

    # 핵심1
    room, floor = divmod(N, H)

    # 핵심2
    if floor == 0:
        floor = H
    else:
        room += 1

    # 핵심3
    space = ""
    if room < 10:
        space = "0"

    print(str(floor) + space + str(room))

"""
- 난이도: 브론즈3
- 분류: 구현
"""
