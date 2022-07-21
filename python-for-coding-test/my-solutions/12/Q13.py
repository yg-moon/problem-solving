# BOJ 15686
from itertools import combinations
INF = 1e9

N, M = map(int, input().split())
city = []
for _ in range(N):
    city.append(list(map(int, input().split())))

houses = []
chickens = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            houses.append((i, j))
        elif city[i][j] == 2:
            chickens.append((i, j))

# M개의 치킨집으로 가능한 모든 조합 만들기
combs = list(combinations(chickens, M))

# 각 조합마다 '도시의 치킨 거리'를 찾고, 최솟값 고르기.
min_city_len = INF
for comb in combs:
    city_len = 0
    for house in houses:
        house_len = INF
        for chicken in comb:
            chicken_len = abs(house[0] - chicken[0]) + abs(house[1] - chicken[1])
            house_len = min(house_len, chicken_len)
        city_len += house_len
    min_city_len = min(min_city_len, city_len)

print(min_city_len)
