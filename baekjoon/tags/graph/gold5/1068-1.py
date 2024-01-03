# 트리
from collections import deque

N = int(input())
parent = list(map(int, input().split()))
erase = int(input())

seen = set()
erase_cnt = 0


def bfs():
    global erase_cnt

    # 핵심1: 노드를 지우면 자손노드도 전부 제외
    q = deque()
    q.append(erase)
    while q:
        idx = q.popleft()
        erase_cnt += 1
        parent[idx] = -2  # 주의: 자기 자신도 제외
        for i in range(N):
            if parent[i] == idx:
                parent[i] = -2
                q.append(i)

    for i in range(N):
        if parent[i] != -2:
            seen.add(parent[i])


bfs()

# 예외처리: 남은 노드가 하나도 없을때
if erase_cnt == N:
    print(0)
# 핵심2: 리프노드 = 부모로 한번도 등장하지 않은 것
else:
    answer = N - erase_cnt - len(seen) + 1
    print(answer)

"""
- 난이도: 골드5
- 분류: 트리
- 소요 시간: 40분

- BFS 풀이

디버깅: 틀렸습니다
- 이유1: 자기 자신도 트리에서 제외해야 함
- 이유2: 모든 노드가 없을때 예외처리 (사실 리프노드 계산법을 바꾸면 필요없음)
- 반례: https://www.acmicpc.net/board/view/96949
"""
