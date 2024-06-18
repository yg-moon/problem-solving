def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N, M, K = map(int, input().split())
candies = [0] + list(map(int, input().split()))

parent = list(range(N + 1))

for _ in range(M):
    kid1, kid2 = map(int, input().split())
    union(kid1, kid2)

info = {}
for i in range(1, N + 1):
    root = find(i)  # 주의: 모든 아이들에 대해 다시 한번 find를 해줘야 함
    if root not in info:
        info[root] = [0, 0]  # [kid, candy]
    info[root][0] += 1
    info[root][1] += candies[i]
info = list(info.values())

# dp[j]: j명의 아이들로 얻을 수 있는 최대 사탕수
dp = [0] * K

for i in range(len(info)):
    kid = info[i][0]
    candy = info[i][1]
    for j in range(K - 1, kid - 1, -1):
        dp[j] = max(dp[j], dp[j - kid] + candy)

print(dp[-1])

"""
- 난이도: 골드3
- 분류: 분리집합 + 냅색
- 소요 시간: 80분
"""
