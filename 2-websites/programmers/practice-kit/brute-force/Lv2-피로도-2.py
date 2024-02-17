from itertools import permutations


def solution(k, dungeons):
    N = len(dungeons)
    max_cnt = 0

    # 각 순열에 대해
    for perm in permutations(range(N)):
        cur_k = k
        cnt = 0
        # 순열의 순서대로 진행
        for p in perm:
            # 현재 피로도 >= 최소 필요 피로도 이면 진행
            if cur_k >= dungeons[p][0]:
                cur_k -= dungeons[p][1]
                cnt += 1
                max_cnt = max(max_cnt, cnt)
            # 아닐 경우 현재 순열은 진행 중지
            else:
                break

    return max_cnt


"""
- 순열을 이용한 완전탐색
"""
