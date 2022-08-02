from collections import defaultdict

V, E = map(int, input().split())

# 부모를 자기 자신으로 초기화
parent = defaultdict(int)
for i in range(1, V + 1):
    parent[i] = i

# Find: Path compression 적용
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


# Union: 더 작은 쪽을 부모로 설정
def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 그래프 생성
# 예시 입력
# 6 4
# 1 4
# 2 3
# 2 4
# 5 6
def make_graph():
    for _ in range(E):
        a, b = map(int, input().split())
        union(a, b)


# 사이클 발생 여부 확인
# 예시 입력
# 3 3
# 1 2
# 1 3
# 2 3
def is_cyclic():
    cycle = False
    for _ in range(E):
        a, b = map(int, input().split())
        # 루트가 같으면 사이클 존재
        if find(a) == find(b):
            cycle = True
            break
        # 루트가 다르면 두 노드를 Union
        else:
            union(a, b)
    return cycle


# Driver code (동시에 돌리지 말 것)

# Option 1:
make_graph()

# Option 2:
# print("Has cycle: ", is_cyclic())


# 출력
print("%-10s" % "Node", end=" ")
for i in range(1, V + 1):
    print(i, end=" ")
print()
print("%-10s" % "Root", end=" ")
for i in range(1, V + 1):
    print(find(i), end=" ")
print()
print("%-10s" % "Parent", end=" ")
for i in range(1, V + 1):
    print(parent[i], end=" ")
print()
