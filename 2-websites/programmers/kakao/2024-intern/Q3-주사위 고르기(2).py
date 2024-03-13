from itertools import combinations
import bisect


def solution(dice):
    N = len(dice)
    seen = set()
    max_win = 0
    answer = []

    for comb1 in combinations(range(1, N + 1), N // 2):
        # 효율성: 이미 계산한 조합이라면 스킵
        if comb1 in seen:
            continue

        comb2 = tuple(x for x in range(1, N + 1) if x not in comb1)
        seen.add(comb1)
        seen.add(comb2)

        result1 = []
        result2 = []

        # 현재 주사위 조합으로 가능한 모든 합을 계산
        def dfs(idx, res, comb, result):
            if idx == len(comb):
                result.append(res)
                return
            for i in range(6):
                dfs(idx + 1, res + dice[comb[idx] - 1][i], comb, result)

        dfs(0, 0, comb1, result1)
        dfs(0, 0, comb2, result2)

        win = 0
        loss = 0
        result2.sort()

        # 효율성: 이분탐색으로 빠르게 계산
        for r1 in result1:
            l = bisect.bisect_left(result2, r1)
            r = bisect.bisect_right(result2, r1)
            win += l
            loss += len(result2) - r

        if win >= loss and win > max_win:
            max_win = win
            answer = comb1
        elif win < loss and loss > max_win:
            max_win = loss
            answer = comb2

    return list(answer)


"""
- 실전에서 제출했던 풀이
- product 대신 재귀로 해결 (성능은 재귀가 더 빠름)
"""
