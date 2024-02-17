from collections import deque

S = int(input())


def bfs():
    q = deque()
    q.append((1, 0))
    dist = [[-1] * (S + 1) for _ in range(S + 1)]
    dist[1][0] = 0  # dist[이모티콘 개수][클립보드 상태] = 최소 시간

    while q:
        cur, clip = q.popleft()

        if cur == S:
            return dist[cur][clip]

        # 1. 화면에 있는 이모티콘을 클립보드에 저장
        # 주의: 아직 방문하지 않았을 때만 갱신
        if dist[cur][cur] == -1:
            q.append((cur, cur))
            dist[cur][cur] = dist[cur][clip] + 1
        # 2. 클립보드에 있는 이모티콘을 붙여넣기
        # 주의: 값이 범위 안에 있는지 체크
        if cur + clip <= S and dist[cur + clip][clip] == -1:
            q.append((cur + clip, clip))
            dist[cur + clip][clip] = dist[cur][clip] + 1
        # 3. 화면에 있는 이모티콘 하나 삭제
        if cur >= 1 and dist[cur - 1][clip] == -1:
            q.append((cur - 1, clip))
            dist[cur - 1][clip] = dist[cur][clip] + 1

    return -1


print(bfs())

"""
dp 풀이
- 2차원 배열을 사용한 해법
- 장점: 메모리 효율
- 단점: 덜 직관적
"""
