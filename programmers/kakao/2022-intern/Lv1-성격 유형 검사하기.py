from collections import defaultdict


def solution(survey, choices):
    # {알파벳: 점수}
    char_to_score = defaultdict(int)

    # 지표별 유형 종류
    types = [["R", "T"], ["C", "F"], ["J", "M"], ["A", "N"]]

    # 알파벳별 점수 계산
    for i in range(len(survey)):
        score = abs(choices[i] - 4)
        if choices[i] < 4:
            char_to_score[survey[i][0]] += score
        elif choices[i] > 4:
            char_to_score[survey[i][1]] += score

    # 지표마다 알파벳 확정
    answer = ""
    for t1, t2 in types:
        if char_to_score[t1] >= char_to_score[t2]:
            answer += t1
        else:
            answer += t2
    return answer
