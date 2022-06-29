import collections

n, m = map(int, input().split())

parent = collections.defaultdict(int)
for i in range(1, n + 1):
    parent[i] = i

ops = []
for _ in range(m):
    ops.append(list(map(int, input().split())))


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


for op, a, b in ops:
    if op == 0:
        union(a, b)
    elif op == 1:
        print("YES") if find(a) == find(b) else print("NO")
