V, E = map(int, input().split())
parent = list(range(V + 1))


def find(x, parent):
    if parent[x] != x:
        parent[x] = find(parent[x], parent)
    return parent[x]


def union(a, b, parent):
    a = find(a, parent)
    b = find(b, parent)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


edges = []
total_cost = 0

for _ in range(E):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

# 간선을 비용순으로 정렬
edges.sort()

for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 MST에 포함 (union)
    if find(a, parent) != find(b, parent):
        union(a, b, parent)
        total_cost += cost

print(total_cost)
