from collections import defaultdict


def solution(friends, gifts):
    info = defaultdict(lambda: defaultdict(int))  # {준 사람: {받은 사람: 개수}}
    score = defaultdict(int)  # {이름: 선물 지수}
    result = []

    for gift in gifts:
        a, b = gift.split()
        info[a][b] += 1
        score[a] += 1
        score[b] -= 1

    for f1 in friends:
        cnt = 0
        for f2 in friends:
            if f1 != f2:
                if info[f1][f2] > info[f2][f1]:
                    cnt += 1
                elif info[f1][f2] == info[f2][f1] and score[f1] > score[f2]:
                    cnt += 1
        result.append(cnt)

    return max(result)


"""
- 분류: 구현
- 소요 시간: 25분

조건
- 주고 받은 기록이 있으면, 더 많이 준 사람이 +1
- 주고 받은 기록이 없거나 같으면
    - 선물 지수가 더 큰 사람이 +1
    - 선물 지수도 같으면 무효
"""
