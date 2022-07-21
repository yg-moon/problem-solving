# Kakao 2020
# from 이코테
from bisect import bisect_left, bisect_right
from collections import defaultdict


# [left, right] 범위에 있는 데이터의 개수를 리턴
def count_by_range(arr, left, right):
    right_idx = bisect_right(arr, right)
    left_idx = bisect_left(arr, left)
    return right_idx - left_idx


def solution(words, queries):
    answer = []
    arr = defaultdict(list)  # 단어들을 길이마다 나누어서 저장
    rev_arr = defaultdict(list)  # 뒤집은 단어들을 길이마다 나누어서 저장

    for word in words:
        arr[len(word)].append(word)
        rev_arr[len(word)].append(word[::-1])

    # 이진탐색을 위해 정렬
    for key in arr:
        arr[key].sort()
        rev_arr[key].sort()

    for q in queries:
        # ?가 뒤에 올 경우
        if q[0] != "?":  
            res = count_by_range(arr[len(q)], q.replace("?", "a"), q.replace("?", "z"))
        # ?가 앞에 올 경우
        else:
            res = count_by_range(
                rev_arr[len(q)],
                q[::-1].replace("?", "a"),
                q[::-1].replace("?", "z"),
            )
        answer.append(res)
    
    return answer
