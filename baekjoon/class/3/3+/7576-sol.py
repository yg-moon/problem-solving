# 토마토
# 출처: https://jae04099.tistory.com/entry/백준-7576-토마토-파이썬-해설포함
from collections import deque

M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

q = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = 0

# 처음 토마토 위치를 큐에 넣기
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            q.append([i, j])

# BFS
while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
            graph[nx][ny] = graph[x][y] + 1
            q.append([nx, ny])

# 그래프 전체를 돌면서 정답 구하기
for row in graph:
    for r in row:
        if r == 0:
            print(-1)
            exit(0)
    answer = max(answer, max(row))
print(answer - 1)

"""
차이점
- 그래프의 값을 직접 바꾸고, 그래프의 상태만으로 정답을 구한다.
- 따라서 visited도 관리할 필요가 없고, 이외의 다른 변수들도 필요가 없다.

코멘트 (효율성 & 확장성에 대해)
- 이 문제에서는 지금 풀이가 훨씬 깔끔하고 간단하다.
- 하지만 문제가 어려워지면 결국 내 풀이처럼 작성해야 한다.
    - ex. 만약 그래프의 값을 직접 바꿀수 없는 경우에는 필요한 정보들을 큐에 함께 넣어야 한다.
    - ex. 만약 그래프의 최종 상태만으로는 정답을 알 수 없는 경우에는 추가 변수를 선언해야 한다.
    - ex. 만약 그래프가 너무 커서 탐색을 여러번 할 수 없을 경우에는 최대한 적게 돌아야 한다.
- 다만 이번처럼 그래프 내에서 해결할 수 있다면 지금처럼 푸는게 훨씬 간편하다.
"""
