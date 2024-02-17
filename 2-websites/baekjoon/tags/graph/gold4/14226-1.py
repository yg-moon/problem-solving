# 이모티콘
from collections import deque

S = int(input())


def bfs():
    q = deque()
    q.append((1, 0, 0))
    visited = set()
    visited.add((1, 0))  # 핵심: (이모티콘 개수, 클립보드 상태)로 방문여부를 기록

    while q:
        cur, clip, time = q.popleft()

        if cur == S:
            return time

        # 1. 화면에 있는 이모티콘을 클립보드에 저장
        # 주의: 화면에 있는걸 비우지 않음
        if (cur, cur) not in visited:
            q.append((cur, cur, time + 1))
            visited.add((cur, cur))
        # 2. 클립보드에 있는 이모티콘을 붙여넣기
        # 주의: 클립보드에 있는걸 비우지 않음
        if (cur + clip, clip) not in visited:
            q.append((cur + clip, clip, time + 1))
            visited.add((cur + clip, clip))
        # 3. 화면에 있는 이모티콘 하나 삭제
        if (cur - 1, clip) not in visited:
            q.append((cur - 1, clip, time + 1))
            visited.add((cur - 1, clip))

    return -1


print(bfs())

"""
- 난이도: 골드4
- 분류: BFS
- 소요 시간: 15분
"""
