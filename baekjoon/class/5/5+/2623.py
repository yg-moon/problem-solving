# 음악프로그램
from collections import defaultdict, deque

N, M = map(int, input().split())

graph = defaultdict(list)
idg = [0] * (N + 1)

for _ in range(M):
    nums = list(map(int, input().split()))
    for i in range(1, nums[0]):
        a = nums[i]
        b = nums[i + 1]
        graph[a].append(b)
        idg[b] += 1


def topo_sort():
    q = deque()
    res = []

    for i in range(1, N + 1):
        if idg[i] == 0:
            q.append(i)

    while q:
        cur = q.popleft()
        res.append(cur)

        for nxt in graph[cur]:
            idg[nxt] -= 1
            if idg[nxt] == 0:
                q.append(nxt)

    return res


result = topo_sort()

if len(result) == N:
    for r in result:
        print(r)
else:
    print(0)

"""
- 난이도: 골드3
- 분류: 위상정렬

- 위상정렬이 가능한지 단순히 확인하면 되는 문제
"""
