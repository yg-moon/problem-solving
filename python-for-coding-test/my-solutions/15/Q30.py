# Kakao 2020
# 출처: 이코테
from bisect import bisect_left, bisect_right
from collections import defaultdict


# [left, right] 범위에 있는 데이터의 개수를 리턴
def count_by_range(arr, left, right):
    right_idx = bisect_right(arr, right)
    left_idx = bisect_left(arr, left)
    return right_idx - left_idx


def solution(words, queries):
    answer = []
    dic = defaultdict(list)  # 단어들을 길이마다 나누어서 저장
    rev_dic = defaultdict(list)  # 뒤집은 단어들을 길이마다 나누어서 저장

    for word in words:
        dic[len(word)].append(word)
        rev_dic[len(word)].append(word[::-1])

    # 이진탐색을 위해 정렬
    for key in dic:
        dic[key].sort()
        rev_dic[key].sort()

    for q in queries:
        # ?가 뒤에 올 경우
        if q[0] != "?":
            cnt = count_by_range(dic[len(q)], q.replace("?", "a"), q.replace("?", "z"))
        # ?가 앞에 올 경우
        else:
            cnt = count_by_range(
                rev_dic[len(q)],
                q[::-1].replace("?", "a"),
                q[::-1].replace("?", "z"),
            )
        answer.append(cnt)

    return answer
