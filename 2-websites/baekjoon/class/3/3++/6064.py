# 카잉 달력
# 출처: https://ji-gwang.tistory.com/m/249
T = int(input())

for _ in range(T):
    M, N, x, y = map(int, input().split())
    k = x
    found = False

    while k <= M * N:
        if (k - x) % M == 0 and (k - y) % N == 0:
            print(k)
            found = True
            break
        k += M

    if not found:
        print(-1)

"""
- 단 한줄의 식으로 정리해서 훨씬 깔끔하다.
"""
