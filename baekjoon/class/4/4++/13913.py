# 숨바꼭질 4
# 출처: https://data-flower.tistory.com/79
from collections import deque

N, K = map(int, input().split())
MAX = 100001

visited = [0] * MAX
prev = [0] * MAX


def get_path(node):
    ret = []
    cur = node
    # 걸리는 시간만큼 반복하면서
    for _ in range(visited[node] + 1):
        # 꼬리물기 방식으로 역추적
        ret.append(cur)
        cur = prev[cur]
    return ret[::-1]


def bfs():
    q = deque([N])
    while q:
        cur = q.popleft()
        if cur == K:
            print(visited[cur])
            print(*get_path(cur))
            return
        for nxt in [cur - 1, cur + 1, 2 * cur]:
            if 0 <= nxt < MAX and visited[nxt] == 0:
                q.append(nxt)
                visited[nxt] = visited[cur] + 1
                prev[nxt] = cur


bfs()

"""
- 난이도: 골드4
- 분류: BFS

핵심
- 경로를 추적하는 문제는 각 노드가 자신의 prev 정보를 갖는 방식으로 해결한다.
- 출력시에는 한쪽 끝부터 시작해서 꼬리물기 방식으로 뽑으면 된다.
"""
