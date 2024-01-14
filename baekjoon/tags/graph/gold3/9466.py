# 텀 프로젝트
import sys

sys.setrecursionlimit(10**6)  # 기본값은 10**3


def dfs(cur):
    global cnt

    visited[cur] = True
    cur_list.append(cur)
    nxt = arr[cur]

    if not visited[nxt]:
        dfs(nxt)
    else:
        if nxt in cur_list:
            # 핵심: 사이클이 되는 구간부터만 팀을 이룸
            cnt += len(cur_list) - cur_list.index(nxt)


T = int(input())

for _ in range(T):
    N = int(input())
    arr = [0] + list(map(int, input().split()))
    visited = [False] * (N + 1)
    cnt = 0

    for i in range(1, N + 1):
        if not visited[i]:
            cur_list = []
            dfs(i)

    print(N - cnt)

"""
- 난이도: 골드3
- 분류: DFS

요약
- 앞에서부터 매번 가능한데까지 DFS로 방문하면서, 현재 방문기록을 따로 관리
- index()를 통해 사이클의 시작위치를 파악하여 팀의 크기를 계산

디버깅: 시간초과
- 한번 방문한 학생은 다시 방문할 필요가 없었음
- 왜냐하면 문제구조상 팀에 소속될 사람은 첫 방문에서 반드시 결성되기 때문

참고
- https://claude-u.tistory.com/435
"""
