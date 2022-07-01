n, m = map(int, input().split())
balls = list(map(int, input().split()))

arr = [0] * 11

# 각 무게에 해당하는 볼링공의 개수 카운트
for b in balls:
    arr[b] += 1

result = 0
# 1부터 m까지의 각 무게에 대하여 처리
for i in range(1, m + 1):
    n -= arr[i] # (B가 선택하는 경우의 수) = (전체 볼링공 수) - (현재 A가 고른 무게의 볼링공 수)
    result += arr[i] * n # (A가 고른 무게의 볼링공 수) * (B가 선택하는 경우의 수)

print(result)
