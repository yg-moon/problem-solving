# 선분 교차 2
x1, y1, x2, y2 = list(map(int, input().split()))
x3, y3, x4, y4 = list(map(int, input().split()))


def ccw(x1, y1, x2, y2, x3, y3):
    return (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)


ccw123 = ccw(x1, y1, x2, y2, x3, y3)
ccw124 = ccw(x1, y1, x2, y2, x4, y4)
ccw341 = ccw(x3, y3, x4, y4, x1, y1)
ccw342 = ccw(x3, y3, x4, y4, x2, y2)
answer = 0

# 평행
if ccw123 * ccw124 == 0 and ccw341 * ccw342 == 0:
    if (
        min(x1, x2) <= max(x3, x4)
        and min(x3, x4) <= max(x1, x2)
        and min(y1, y2) <= max(y3, y4)
        and min(y3, y4) <= max(y1, y2)
    ):
        answer = 1
# 교차
elif ccw123 * ccw124 <= 0 and ccw341 * ccw342 <= 0:
    answer = 1

print(answer)

"""
- 난이도: 골드2
- 분류: 기하

- 참고: https://rccode.tistory.com/159
"""
