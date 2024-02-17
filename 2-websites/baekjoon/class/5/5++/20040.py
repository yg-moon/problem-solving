# 사이클 게임
# 출처: https://computer-science-student.tistory.com/675
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
parent = list(range(n))


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


for i in range(1, m + 1):
    p1, p2 = map(int, input().split())
    if find(p1) == find(p2):
        print(i)
        exit(0)
    union(p1, p2)

print(0)

"""
- 난이도: 골드4
- 분류: 분리 집합(union-find)

핵심
- 무방향 그래프에서는 union-find로 사이클을 판별할 수 있다.
- (방향 그래프에서는 DFS를 사용)
"""
