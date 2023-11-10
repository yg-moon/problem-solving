# 게리맨더링
from collections import defaultdict, deque

N = int(input())
peoples = [0] + list(map(int, input().split()))  # 1-idx

graph = defaultdict(list)
min_diff = int(1e9)

for i in range(1, N + 1):
    for num in list(map(int, input().split()))[1:]:
        graph[i].append(num)


# 핵심3: 그룹이 모두 연결되어 있는지 확인하고, 총 인구수를 리턴 (연결이 안 되었다면 -1)
def bfs(group):
    q = deque()
    q.append(group[0])
    bfs_visited = [False] * (N + 1)
    bfs_visited[group[0]] = True
    nodes_cnt = 0
    people_sum = 0

    while q:
        cur = q.popleft()
        nodes_cnt += 1
        people_sum += peoples[cur]

        # 인접한 노드가 그룹에 속해 있다면 진행
        for nxt in graph[cur]:
            if nxt in group and not bfs_visited[nxt]:
                bfs_visited[nxt] = True
                q.append(nxt)

    # 그룹이 모두 연결되었다 <-> BFS 결과의 길이가 그룹의 길이와 같다
    return people_sum if nodes_cnt == len(group) else -1


def dfs(depth, start, target_size):
    global min_diff

    if depth == target_size:
        group1 = [i for i in range(1, N + 1) if visited[i]]
        group2 = [i for i in range(1, N + 1) if not visited[i]]
        cnt1 = bfs(group1)
        cnt2 = bfs(group2)
        if cnt1 == -1 or cnt2 == -1:
            return
        min_diff = min(min_diff, abs(cnt1 - cnt2))
        return

    # 핵심2: visited 상태의 조합을 만들기
    for i in range(start, N + 1):
        visited[i] = True
        dfs(depth + 1, i + 1, target_size)
        visited[i] = False


# 핵심1: 각 목표 크기에 대해 그룹화 (팁: 절반까지만 진행해도 됨)
for i in range(1, (N // 2) + 1):
    visited = [False] * (N + 1)
    dfs(0, 1, i)

if min_diff != int(1e9):
    print(min_diff)
else:
    print(-1)

"""
- 난이도: 골드4
- 분류: 브루트포스, BFS, 조합

요약
- 목표: 두 선거구로 나누었을때 인구차의 최솟값
- 방법: 모든 경우를 시도 (단, 선거구 조건을 만족해야 함)

디버깅
- 1. (구현 실수) BFS에서 시작노드 방문처리를 까먹었다.
- 2. (구현 실수) for nxt in graph[node]를 range(len(graph[node])))로 썼다.
- 3. (접근법 오류) DFS로 선거구를 찾으려한게 문제였다.
    - 조합으로 그룹을 찾고, 나누어진 두 그룹이 인접한지는 BFS로 확인해야 한다.
    - 참고: https://www.acmicpc.net/board/view/42505
"""
