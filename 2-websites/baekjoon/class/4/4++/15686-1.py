# 치킨 배달
INF = int(1e9)

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

houses = []
all_chickens = []
cur_chickens = []
answer = INF

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            houses.append((i, j))
        elif graph[i][j] == 2:
            all_chickens.append((i, j))

visited = [False] * len(all_chickens)


# 현재 조합에서 도시의 치킨거리 계산
def calc():
    city_dist = 0
    for hi, hj in houses:
        house_dist = INF
        for ci, cj in cur_chickens:
            house_dist = min(house_dist, abs(hi - ci) + abs(hj - cj))
        city_dist += house_dist
    return city_dist


# 길이가 M인 모든 조합에 대해 백트래킹으로 시도
def dfs(start):
    global answer
    if len(cur_chickens) == M:
        answer = min(answer, calc())
        return
    else:
        for i in range(start, len(all_chickens)):
            if not visited[i]:
                visited[i] = True
                cur_chickens.append(all_chickens[i])
                dfs(i + 1)  # 주의: start+1 이 아니라 i+1로 해야 불필요한 중복을 방지
                cur_chickens.pop()
                visited[i] = False


dfs(0)

print(answer)

"""
- 난이도: 골드5
- 분류: 구현, 브루트포스, 백트래킹
"""
