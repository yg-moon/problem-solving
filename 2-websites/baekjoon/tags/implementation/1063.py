# 킹
king, stone, N = input().split()


def out_of_bounds(pos):
    return not ("A" <= pos[0] <= "H" and "1" <= pos[1] <= "8")


dir = {
    "R": (1, 0),
    "L": (-1, 0),
    "B": (0, -1),
    "T": (0, 1),
    "RT": (1, 1),
    "LT": (-1, 1),
    "RB": (1, -1),
    "LB": (-1, -1),
}

for _ in range(int(N)):
    move = input()
    dx, dy = dir[move]
    next_king = chr(ord(king[0]) + dx) + str(int(king[1]) + dy)

    if out_of_bounds(next_king):
        continue

    if next_king == stone:
        next_stone = chr(ord(stone[0]) + dx) + str(int(stone[1]) + dy)
        if out_of_bounds(next_stone):
            continue
        stone = next_stone

    # 주의: 돌이 무효가 되면 왕도 무효이므로 마지막에 이동
    king = next_king

print(king)
print(stone)

"""
- 난이도: 실버3
- 분류: 구현, 시뮬레이션

핵심
- dx, dy를 이용해서 간단하게 작성
"""
