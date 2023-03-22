# 터렛
# 출처: https://ooyoung.tistory.com/111
T = int(input())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

    # 동심원이고 반지름이 같을 때
    if d == 0 and r1 == r2:
        print(-1)
    # 내접, 외접일 때
    elif abs(r1 - r2) == d or r1 + r2 == d:
        print(1)
    # 두 원이 서로 다른 두 점에서 만날 때
    elif abs(r1 - r2) < d < (r1 + r2):
        print(2)
    # 그 외의 경우
    else:
        print(0)

"""
- 난이도: 실버3
- 분류: 기하
"""
