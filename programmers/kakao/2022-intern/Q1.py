import collections


def solution(survey, choices):
    # 각 타입에 대한 점수
    type_to_score = collections.defaultdict(int)

    # 점수 변환표
    score_conversion = {
        1: 3,
        2: 2,
        3: 1,
        4: 0,
        5: 1,
        6: 2,
        7: 3
    }

    # 점수 채우기
    for i in range(len(survey)):
        # 점수가 1,2,3 이면 왼쪽이 3,2,1 점
        if choices[i] < 4:
            type_to_score[survey[i][0]] += score_conversion[choices[i]]
        # 점수가 5,6,7 이면 오른쪽이 1,2,3 점
        else:
            type_to_score[survey[i][1]] += score_conversion[choices[i]]

    # 결과 구하기
    answer = []
    indicators = [["R", "T"], ["C", "F"], ["J", "M"], ["A", "N"]]
    for types in indicators:
        # 주의: 동점일 경우 사전순.
        if type_to_score[types[0]] >= type_to_score[types[1]]:
            answer.append(types[0])
        else:
            answer.append(types[1])
    return "".join(answer)
