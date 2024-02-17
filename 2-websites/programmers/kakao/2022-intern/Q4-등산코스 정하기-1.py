from collections import defaultdict


def solution(n, paths, gates, summits):
    graph = defaultdict(list)
    gates_set = set(gates)
    summits_set = set(summits)
    summit_res = int(1e9)
    min_intensity = int(1e9)

    for i, j, w in paths:
        graph[i].append((j, w))
        graph[j].append((i, w))

    def dfs(start, cur, intensity, reached_summit, summit):
        nonlocal summit_res, min_intensity

        # 탐색 조기종료
        if intensity > min_intensity:
            return

        # 등산코스를 완성한 경우
        if start == cur and reached_summit:
            if intensity < min_intensity or (
                intensity == min_intensity and summit < summit_res
            ):
                summit_res = summit
                min_intensity = intensity
            return

        # 연결된 모든 노드 방문시도
        for nxt, w in graph[cur]:
            if visited[nxt] < 2:
                visited[nxt] += 1
                if nxt in gates_set:
                    if nxt == start and reached_summit:
                        dfs(
                            start,
                            nxt,
                            max(intensity, w),
                            reached_summit,
                            summit,
                        )
                elif nxt in summits_set:
                    if not reached_summit:
                        dfs(start, nxt, max(intensity, w), True, nxt)
                else:
                    dfs(
                        start,
                        nxt,
                        max(intensity, w),
                        reached_summit,
                        summit,
                    )
                visited[nxt] -= 1

    # 모든 gate에서 출발하기
    for gate in gates:
        visited = [0] * (n + 1)
        dfs(gate, gate, 0, False, 0)

    return [summit_res, min_intensity]


"""
- 백트래킹 풀이 (시간초과)
- 소요 시간:
    - 8:00-8:45 (45분) (1차 시도, 25개중 13개 시간초과)
    - 8:45-9:05 (20분) (2차 시도, 모르겠다...)

조건
- 하나의 gate에서 시작
- 하나의 summit만 방문
- 다시 원래 gate로 돌아옴
- 경로의 가중치의 최소값 intensity

백트래킹
- 모든 gate에서 시작해보기
- 연결된 모든 경로로 가보기
    - 조건을 만족하지 않으면 후퇴
        - 반드시 1개의 summit
        - 처음과 끝에서만 같은 gate
        - 최소 intensity

디버깅
- 1. 예제 틀림 -> 중복방문이 가능하므로 visited를 없애야 함
- 2. 예제에서 재귀깊이 초과 -> 휴식처간 무한재방문 이슈: 2번까지만 허용
- 3. 시간초과 -> 모르겠음
"""
