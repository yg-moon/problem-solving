# LCD Test
s, n = map(int, input().split())
nums = list(str(n))
screen = [[" "] * (s + 3) * len(nums) for _ in range(2 * s + 3)]


def row1(i):
    for j in range(i + 1, i + 1 + s):
        screen[0][j] = "-"


def row2(i):
    for j in range(i + 1, i + 1 + s):
        screen[s + 1][j] = "-"


def row3(i):
    for j in range(i + 1, i + 1 + s):
        screen[2 * s + 2][j] = "-"


def col1(i):
    for j in range(1, 1 + s):
        screen[j][i] = "|"


def col2(i):
    for j in range(1, 1 + s):
        screen[j][i + s + 1] = "|"


def col3(i):
    for j in range(s + 2, 2 * s + 2):
        screen[j][i] = "|"


def col4(i):
    for j in range(s + 2, 2 * s + 2):
        screen[j][i + s + 1] = "|"


num_to_funcs = {
    "1": [col2, col4],
    "2": [row1, row2, row3, col2, col3],
    "3": [row1, row2, row3, col2, col4],
    "4": [row2, col1, col2, col4],
    "5": [row1, row2, row3, col1, col4],
    "6": [row1, row2, row3, col1, col3, col4],
    "7": [row1, col2, col4],
    "8": [row1, row2, row3, col1, col2, col3, col4],
    "9": [row1, row2, row3, col1, col2, col4],
    "0": [row1, row3, col1, col2, col3, col4],
}


def draw(i, num):
    for func in num_to_funcs[num]:
        func(i)


for i, num in enumerate(nums):
    draw((s + 3) * i, num)

for row in screen:
    for c in row:
        print(c, end="")
    print()

"""
- 요약: 주어진 그대로 구현
- 구현
    - 전체 배열을 생성해두고 알맞은 위치에 각 숫자마다 패턴대로 채운다.
    - 각 숫자도 모듈별로 표현을 나눌 수 있다. (row1 ~ row3, col1 ~ col4)
"""
