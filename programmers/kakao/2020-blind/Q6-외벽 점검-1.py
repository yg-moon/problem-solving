def solution(n, weak, dist):
    # 원형배열 구현
    new_weak = weak + [w + n for w in weak]

    # 거리 역순으로 정렬
    dist.sort(reverse=True)

    # 최소 인원수
    min_cnt = len(dist) + 1

    def dfs(idx, fixed, cnt):
        nonlocal min_cnt
        if idx >= len(dist) or cnt >= min_cnt:
            return
        # 모든 weak를 출발점으로 해서
        for i in range(len(weak)):
            new_fixed = set()
            for j in range(i, i + len(weak)):
                if new_weak[j] <= weak[i] + dist[idx]:
                    new_fixed.add(new_weak[j] % n)
                else:
                    break
            # 취약점을 모두 점검할 수 있으면 정답 갱신
            union_fixed = fixed.union(new_fixed)
            if len(union_fixed) == len(weak):
                min_cnt = min(min_cnt, cnt)
                return
            # 아니라면 재귀
            dfs(idx + 1, union_fixed, cnt + 1)

    dfs(0, set(), 1)

    return min_cnt if min_cnt <= len(dist) else -1


"""
- (시간초과)
- 소요 시간:
    - 11:10-12:30 (90분) -> 계획
    - 3:30-3:40 (10분) -> 재귀로 구현 (25개중 7개 시간초과)
    - 3:40-4:30 (50분) -> 시간초과 디버깅하다가 포기.
"""
