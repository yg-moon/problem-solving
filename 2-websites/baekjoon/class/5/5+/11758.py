# CCW


# x1 x2 x3 x1
# y1 y2 y3 y1
# 우측 대각끼리 곱해서 더하고, 좌측 대각끼리 곱해서 빼기
def ccw(x1, y1, x2, y2, x3, y3):
    return x1 * y2 + x2 * y3 + x3 * y1 - x2 * y1 - x3 * y2 - x1 * y3


x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
res = ccw(x1, y1, x2, y2, x3, y3)

if res > 0:  # 양수: 반시계
    print(1)
elif res < 0:  # 음수: 시계
    print(-1)
else:  # 0: 평행
    print(0)

"""
- 난이도: 골드5
- 분류: 기하

- 참고: https://growth-coder.tistory.com/163
"""
