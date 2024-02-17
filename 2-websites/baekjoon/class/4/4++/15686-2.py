# 치킨 배달
from itertools import combinations

INF = int(1e9)

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

houses = []
chickens = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            houses.append((i, j))
        elif graph[i][j] == 2:
            chickens.append((i, j))

# M개의 치킨집 조합 만들기
combs = list(combinations(chickens, M))

# 각 조합마다 '도시의 치킨 거리'를 찾고, 최솟값 고르기.
answer = INF
for comb in combs:
    city_dist = 0
    for house in houses:
        house_dist = INF
        for chicken in comb:
            tmp = abs(house[0] - chicken[0]) + abs(house[1] - chicken[1])
            house_dist = min(house_dist, tmp)
        city_dist += house_dist
    answer = min(answer, city_dist)

print(answer)

"""
- itertools.combinations
"""
