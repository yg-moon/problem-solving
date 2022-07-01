# target = 1 에서 시작해서, 매번 동전의 가치만큼 올려주고, 동전이 더 클 경우 종료.
n = int(input())
coins = list(map(int, input().split()))

coins.sort()

target = 1
for coin in coins:
    # 만들 수 없는 금액을 찾았을 때 반복 종료
    if target < coin:
        break
    target += coin

# 만들 수 없는 금액 출력
print(target)
