# 출처: 이코테

# 다익스트라 정보
# - 인접 행렬
# - dist 타입: dict
# - 파알인 로직
import heapq
import sys
from collections import defaultdict

INF = int(1e9)
input = sys.stdin.readline  # 팁: 입력 빠르게 받기

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = []

T = int(input())
for _ in range(T):
    N = int(input())
    # Adjacent Matrix (인접 행렬) 그래프
    graph = []
    for _ in range(N):
        graph.append(list(map(int, input().split())))

    # 다익스트라
    dist = defaultdict(lambda: defaultdict(int))  # 팁: defaultdict 중첩하기
    Q = [(graph[0][0], 0, 0)]
    while Q:
        time, x, y = heapq.heappop(Q)
        if dist[x][y] == 0:
            dist[x][y] = time
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < N:
                    alt = time + graph[nx][ny]
                    heapq.heappush(Q, (alt, nx, ny))

    answer.append(dist[N - 1][N - 1])

for a in answer:
    print(a)
