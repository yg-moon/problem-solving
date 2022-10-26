from collections import defaultdict


def solution(clothes):
    # dic: {옷 종류: 개수}
    dic = defaultdict(int)
    for cloth in clothes:
        dic[cloth[1]] += 1

    # 모든 종류의 (개수+1)을 누적으로 곱한다. (각 종류를 입지 않는 경우까지 고려)
    answer = 1
    for key in dic:
        answer *= dic[key] + 1

    # 아무것도 입지 않은 경우를 제외해야 하므로 마지막에 -1
    return answer - 1
