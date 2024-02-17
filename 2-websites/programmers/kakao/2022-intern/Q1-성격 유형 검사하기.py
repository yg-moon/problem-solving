from collections import defaultdict


def solution(survey, choices):
    N = len(survey)
    types = [["R", "T"], ["C", "F"], ["J", "M"], ["A", "N"]]
    alp_cnt_dic = defaultdict(int)  # {알파벳: 점수}
    answer = ""

    # 알파벳별 점수 계산
    for i in range(N):
        # 4 미만은 첫번째 글자의 가중치
        if choices[i] < 4:
            alp_cnt_dic[survey[i][0]] += 4 - choices[i]
        # 4 초과는 두번째 글자의 가중치
        elif choices[i] > 4:
            alp_cnt_dic[survey[i][1]] += choices[i] - 4

    # 지표마다 알파벳 확정
    for t1, t2 in types:
        # 동일할 경우 사전순으로 빠르게
        if alp_cnt_dic[t1] >= alp_cnt_dic[t2]:
            answer += t1
        else:
            answer += t2

    return answer


"""
- 분류: 구현
- 소요 시간: 2:05-2:15 (10분)
"""
