# BOJ 18310
# 구현만 살짝 다름
N = int(input())
houses = list(map(int, input().split()))

houses.sort()

if N % 2 == 0:
    print(houses[N // 2 - 1])
else:
    print(houses[N // 2])
