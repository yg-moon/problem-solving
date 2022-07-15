from collections import defaultdict


def solution(clothes):
    # dic: {옷 종류: 개수}
    dic = defaultdict(int)
    for cloth in clothes:
        dic[cloth[1]] += 1

    # 옷의 개수를 모두 배열에 넣는다.
    arr = []
    for key in dic:
        arr.append(dic[key])

    # 배열의 모든 (원소+1)를 곱한다.
    answer = 1
    for i in range(len(arr)):
        answer *= arr[i] + 1

    # 아무것도 입지 않은 경우를 제외해야 하므로 추가로 -1
    return answer - 1
