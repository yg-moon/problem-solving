from collections import defaultdict


def solution(N, stages):
    # {스테이지: 도달 인원수}
    dic = defaultdict(int)
    for i in range(len(stages)):
        dic[stages[i]] += 1

    # [(스테이지, 실패율)]
    answer = []
    total = len(stages)
    for i in range(1, N + 1):
        if i in dic:
            fail = dic[i] / total
            answer.append((i, fail))
            total -= dic[i]
        else:
            answer.append((i, 0))

    answer.sort(key=lambda x: (-x[1], x[0]))
    answer = [x[0] for x in answer]

    return answer
