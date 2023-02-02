# 숨바꼭질 2
# 출처: https://aia1235.tistory.com/40
from collections import deque

N, K = map(int, input().split())
MAX = 100001

q = deque([[N, 0]])
visited = [0] * MAX  # 방문여부 & 몇초에 도달했는지 저장

ans_time = MAX - 1
ans_way = 0

while q:
    cur, time = q.popleft()
    # 이미 최소시간을 초과한 경우는 패스
    if time > ans_time:
        continue
    if cur == K:
        ans_time = time
        ans_way += 1
    for nxt in [cur - 1, cur + 1, 2 * cur]:
        # 해결책1
        if 0 <= nxt < MAX and (visited[nxt] == 0 or visited[nxt] == time + 1):
            q.append([nxt, time + 1])
            visited[nxt] = time + 1

print(ans_time)
print(ans_way)

"""
- 난이도: 골드4
- 분류: BFS

디버깅
- 원인: 방문여부만 따질게 아니라, 경로가 다른 경우를 구분해야 한다.
    - ex. 1->2->3 (+1,+1) 과 1->2->3 (*2,+1) 에서 +1과 *2는 다른 경우다.
- 해결책1: 다음 위치가 이미 방문된 상태라도, 값이 '현재 위치의 time + 1'과 같다면 큐에 넣음. (같은 레벨이므로)

팁
- visited를 배열로 처리하면, 방문여부 뿐만 아니라 해당 위치의 도착시간까지도 기록할 수 있다.
"""
