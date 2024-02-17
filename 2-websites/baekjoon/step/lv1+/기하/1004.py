# 어린 왕자
# 출처: https://pacific-ocean.tistory.com/108
T = int(input())

for _ in range(T):
    cnt = 0
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())

    for _ in range(n):
        cx, cy, r = map(int, input().split())
        d1 = (((x1 - cx) ** 2) + ((y1 - cy) ** 2)) ** 0.5
        d2 = (((x2 - cx) ** 2) + ((y2 - cy) ** 2)) ** 0.5
        if (d1 < r and d2 > r) or (d1 > r and d2 < r):
            cnt += 1

    print(cnt)

"""
- 난이도: 실버3
- 분류: 기하

요약
- 출발점과 도착점이 매번 주어지는 원에 속하는지 확인한다.
    - 둘 다 속하거나, 둘 다 속하지 않으면 진입이나 이탈을 할 필요가 없다.
    - 따라서 하나는 속하고, 하나는 속하지 않을때 cnt를 1 증가시킨다.
"""
