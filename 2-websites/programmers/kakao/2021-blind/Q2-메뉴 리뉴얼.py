from itertools import combinations
from collections import defaultdict


def solution(orders, course):
    answer = []

    # 각 코스의 길이에 대해
    for comb_len in course:
        comb_set = set()
        dic = defaultdict()  # {요리 조합: 주문 횟수}

        # 효율성: 각 주문에서 나올 수 있는 조합만 고려
        for order in orders:
            for comb in combinations(order, comb_len):
                comb_set.add("".join(sorted(comb)))  # 주의: 중복을 고려해서 정렬

        # 해당 조합이 등장한 횟수를 세기
        for comb in comb_set:
            cnt = 0
            for order in orders:
                flag = True
                for c in comb:
                    if c not in order:
                        flag = False
                        break
                if flag:
                    cnt += 1
            # 2명 이상 주문한 조합만 고려
            if cnt >= 2:
                dic[comb] = cnt

        # 가장 주문 횟수가 많은 조합을 정답에 추가
        lst = sorted(dic.items(), key=lambda x: -x[1])

        if lst:
            max_cnt = lst[0][1]
            for comb, cur_len in lst:
                if cur_len == max_cnt:
                    answer.append("".join(sorted(comb)))
                else:
                    break

    return sorted(answer)


"""
- 분류: 조합, 구현

요약
- course 값이 곧 찾을 조합의 길이
- 들어온 알파벳들이 조합의 후보
- 해당 길이의 조합을 만들어서, 몇 명이 해당하는지 카운팅
- 가장 카운트가 많은 조합을 정답에 추가

디버깅: 시간초과
- 원인: 살펴보는 조합 개수가 너무 많았음
- 해결: 들어온 알파벳 전체에서 조합을 찾는게 아니라, 각 주문에서 나올 수 있는 조합에서만 찾기
- 참고: https://school.programmers.co.kr/questions/19338
"""
