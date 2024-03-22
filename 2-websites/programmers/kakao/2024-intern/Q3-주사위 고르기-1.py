from itertools import combinations, product
import bisect


def solution(dice):
    N = len(dice)
    seen = set()
    max_win = 0
    answer = []

    for comb1 in combinations(range(N), N // 2):
        # 효율성: 이미 계산한 조합이라면 스킵
        if comb1 in seen:
            continue

        comb2 = tuple(x for x in range(N) if x not in comb1)
        seen.add(comb1)
        seen.add(comb2)

        result1 = []
        result2 = []

        # 현재 주사위 조합으로 가능한 모든 합의 경우의 수 구하기
        for eye_prod in product(range(6), repeat=len(comb1)):
            val1 = 0
            val2 = 0
            for i in range(len(comb1)):
                val1 += dice[comb1[i]][eye_prod[i]]
                val2 += dice[comb2[i]][eye_prod[i]]
            result1.append(val1)
            result2.append(val2)

        result2.sort()
        win = 0
        loss = 0

        # 효율성: 이분탐색으로 빠르게 계산
        for r1 in result1:
            win += bisect.bisect_left(result2, r1)
            loss += len(result2) - bisect.bisect_right(result2, r1)

        if win >= loss and win > max_win:
            max_win = win
            answer = comb1
        elif loss > win and loss > max_win:
            max_win = loss
            answer = comb2

    return sorted(x + 1 for x in answer)


"""
- 분류: 완전탐색, 이분탐색
- 소요 시간: 1시간

요약: 모든 경우를 시도
- 1. 주사위 n/2개를 고르는 조합
    - 재귀 또는 combinations로 가능
    - 효율성: 반대 조합은 승패가 역이므로 계산을 생략 가능
- 2. 주사위 조합이 주어졌을때 승패판정
    - [A의 가능한 모든 합 가짓수]의 원소로 [B의 가능한 모든 합 가짓수]에 대해 확인
    - 재귀 또는 product로 가능
    - 효율성: 이분탐색으로 빠르게 승패계산
"""
