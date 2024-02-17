# ACM Craft
from collections import defaultdict, deque
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    time = [0] + list(map(int, input().split()))  # 1-idx
    graph = defaultdict(list)
    idg = [0] * (N + 1)
    for _ in range(K):
        X, Y = map(int, input().split())
        graph[X].append(Y)
        idg[Y] += 1
    W = int(input())

    def topo_sort():
        dp = time[:]  # 복사본
        q = deque()
        for i in range(1, N + 1):
            if idg[i] == 0:
                q.append(i)
        while q:
            cur = q.popleft()
            for nxt in graph[cur]:
                # 핵심: 해당 노드까지의 최댓값을 기록
                # 주의: dp/time, cur/nxt 차이를 이해하기
                dp[nxt] = max(dp[nxt], dp[cur] + time[nxt])
                idg[nxt] -= 1
                if idg[nxt] == 0:
                    q.append(nxt)
        return dp[W]

    print(topo_sort())

"""
- 난이도: 골드3
- 분류: 위상정렬 + DP

요약
- 해당 노드까지의 최댓값을 기록하는 대표적인 위상정렬 + DP 유형

메모
- 질문: 구하는건 '건물 W를 건설완료 하는데 드는 최소 시간'인데 왜 최댓값을 계산하는지?
- 답: 문제를 잘 살펴보자.
    W를 완성하려면 이전 건설순서를 갖는 모든 건물이 완성되어야 하고,
    그중에서도 가장 오래 걸린 건물이 기준이 되기 때문.
"""
