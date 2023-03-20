# 하노이 탑 이동 순서
def hanoi(n, a, b, c):
    global K
    if n == 1:
        K += 1
        result.append((a, c))
    else:
        hanoi(n - 1, a, c, b)  # n-1개를 a -> b 이동
        hanoi(1, a, b, c)  # 1개를 a -> c 이동
        hanoi(n - 1, b, a, c)  # n-1개를 b -> c 이동


N = int(input())
K = 0
result = []

hanoi(N, 1, 2, 3)

print(K)
for r in result:
    print(*r)

"""
- 난이도: 실버1
- 분류: 재귀

- 잘 알려진 하노이탑 문제.
"""
