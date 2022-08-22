N = int(input())
coins = list(map(int, input().split()))

coins.sort()

target = 1
for c in coins:
    # 현재 동전이 목표보다 크다면, 이 금액은 만들 수 없다.
    if target < c:
        break
    target += c

print(target)
