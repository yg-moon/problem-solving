# 여행 가자
N = int(input())
M = int(input())
mat = [list(map(int, input().split())) for _ in range(N)]
cities = list(map(int, input().split()))

parent = list(range(N + 1))
is_possible = True


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


# 유니온으로 연결
for i in range(N):
    # 효율성: 삼각형 모양으로 전체의 절반만 탐색해도 됨
    # 주의: 잘못된 삼각형을 택하면 안됨
    for j in range(i + 1):
        # 주의: 조건을 확인하고 합쳐야 함
        if mat[i][j] == 1:
            union(i + 1, j + 1)

# 계획 전체가 연결되었는지 확인
for i in range(M - 1):
    if find(cities[i]) != find(cities[i + 1]):
        is_possible = False
        break

if is_possible:
    print("YES")
else:
    print("NO")

"""
- 난이도: 골드4
- 분류: 분리 집합
- 소요 시간: 20분

핵심
- 문제 잘 읽기: A->B로 가는 직접경로가 없더라도, 간접경로로 도착할 수 있다면 가능한 것으로 판정
- 따라서 유니온 파인드를 사용
"""
