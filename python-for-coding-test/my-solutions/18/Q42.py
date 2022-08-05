# 출처: 이코테
from collections import defaultdict

G = int(input())
P = int(input())
data = []
for _ in range(P):
    data.append(int(input()))

parent = defaultdict(int)
for i in range(1, G + 1):
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


answer = 0

for d in data:
    root = find(d)
    # 루트가 0이면 도킹 불가
    if root == 0:
        break
    # 도킹: 바로 왼쪽의 탑승구 집합과 union
    union(root, root - 1)
    answer += 1

print(answer)
