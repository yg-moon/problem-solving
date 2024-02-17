# 게임 개발
from collections import defaultdict, deque

N = int(input())

graph = defaultdict(list)
idg = [0] * (N + 1)
arr = [0] * (N + 1)

for i in range(1, N + 1):
    t, *reqs, _ = map(int, input().split())
    arr[i] = t
    for r in reqs:
        graph[r].append(i)
        idg[i] += 1


def topo_sort():
    q = deque()
    dp = arr[:]  # 핵심: dp와 arr를 별개로 분리하기

    for i in range(1, N + 1):
        if idg[i] == 0:
            q.append(i)

    while q:
        cur = q.popleft()

        for nxt in graph[cur]:
            # 주의: 점화식을 정확하게 작성하기
            dp[nxt] = max(dp[nxt], dp[cur] + arr[nxt])
            idg[nxt] -= 1
            if idg[nxt] == 0:
                q.append(nxt)

    return dp


result = topo_sort()

for i in range(1, N + 1):
    print(result[i])

"""
- 난이도: 골드3
- 분류: 위상정렬 + DP
- 소요 시간: 35분 (풀이 15분, 디버깅 20분)

요약
- #1005(ACM Craft)와 동일한 문제

디버깅: 출력 초과
- 점화식이 틀렸던게 원인
"""
