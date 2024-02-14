def solution(lottos, win_nums):
    max_rank = 0
    min_rank = 0

    for l in lottos:
        if l in win_nums:
            min_rank += 1
            max_rank += 1
        elif l == 0:
            max_rank += 1

    ranks = [6, 6, 5, 4, 3, 2, 1]
    return [ranks[max_rank], ranks[min_rank]]


""""
- 난이도: Lv1
- 분류: 구현
- 소요시간: 15분 (1차 10분, 2차 5분)

핵심
- 무지성 완탐이 아니라, 효율적인 방법으로 접근하기

요약
- 일단 원래 몇 개나 매칭하는지 계산 (최소)
- 0이 몇 개 있는지 세고, 더하기 (최대)

디버깅: 시간초과
- 완전탐색으로 풀었더니 터짐 (0의 자리에 1~45를 다 넣어보기)
- 45^6 = 83억이기 때문... 구현 전에 미리 계산해보기
"""
