from collections import defaultdict
import bisect


def solution(info, query):
    dic = defaultdict(list)  # {그룹: [점수들]}
    answer = []

    for person in info:
        a, b, c, d, e = person.split()
        e = int(e)
        for na in [a, "-"]:
            for nb in [b, "-"]:
                for nc in [c, "-"]:
                    for nd in [d, "-"]:
                        dic[(na, nb, nc, nd)].append(e)

    # 주의: 한번씩만 정렬하기
    for key in dic:
        dic[key].sort()

    for q in query:
        a, b, c, d = q.split(" and ")
        d, e = d.split()
        e = int(e)

        scores = dic[(a, b, c, d)]
        idx = bisect.bisect_left(scores, e)
        answer.append(len(scores) - idx)

    return answer


"""
- 분류: 이분탐색

해설
- 각 지원자를 2*2*2*2 = 16가지 그룹에 넣어두고, 점수를 정렬
- 기준을 넘는 점수의 개수는 이분탐색으로 빠르게 찾기

느낀점
- 항상 작은 수에 대해서는 완전탐색의 가능성을 고려하기
- 기준을 만족하는 개수를 찾을 때는 이분탐색를 고려하기
"""
