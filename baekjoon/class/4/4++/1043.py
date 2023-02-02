# 거짓말
# 출처: https://velog.io/@dasd412/백준-1043-거짓말-파이썬
N, M = map(int, input().split())
truth = list(map(int, input().split()))[1:]
parties = [list(map(int, input().split()))[1:] for _ in range(M)]
parent = list(range(N + 1))

# 진실을 아는 사람은 부모를 0으로 둠
for person in truth:
    parent[person] = 0


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 파티마다 모든 사람들을 union
for party in parties:
    for i in range(len(party) - 1):
        union(parent, party[i], party[i + 1])

# 파티마다 모든 사람들을 find
# 아무도 진실을 모르는 파티마다 정답 +1
answer = 0
for party in parties:
    for person in party:
        if find(parent, person) == 0:
            break
    else:
        answer += 1
print(answer)

"""
- 난이도: 골드4
- 분류: 분리 집합

디버깅
- 상황: '틀렸습니다'
- 이유: 파티의 모든 사람들을 항상 union 해야 되는데, 진실을 아는 사람이 있을 때만 union 했었음.
"""
