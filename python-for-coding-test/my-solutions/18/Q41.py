from collections import defaultdict

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
plan = list(map(int, input().split()))

parent = defaultdict(int)
for i in range(1, N + 1):
    parent[i] = i


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 or graph[j][i] == 1:
            # 현재 그래프는 0-idx 이므로 +1
            union(i + 1, j + 1)

# plan 내의 모든 루트가 동일한지 확인
possible = True
root = find(plan[0])
for p in plan:
    if find(p) != root:
        possible = False

if possible:
    print("YES")
else:
    print("NO")
