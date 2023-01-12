# 카잉 달력
import math

T = int(input())

for _ in range(T):
    M, N, x, y = map(int, input().split())
    k = x
    found = False
    lcm = math.lcm(M, N)

    while k <= lcm:
        mod = k % N
        if mod == 0:
            mod = N
        if mod == y:
            print(k)
            found = True
            break
        # 핵심: 1씩 올리면 시간초과이므로 M씩 올림
        k += M

    if not found:
        print(-1)

"""
- 난이도: 실버1
- 분류: 수학
"""
