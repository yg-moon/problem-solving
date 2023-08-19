from collections import defaultdict
from bisect import bisect_left, bisect_right


def count_in_range(arr, l, r):
    l_idx = bisect_left(arr, l)
    r_idx = bisect_right(arr, r)
    return r_idx - l_idx


def solution(words, queries):
    answer = []
    rev_words = [word[::-1] for word in words]
    len_words_dic = defaultdict(list)  # {길이: [단어들]}
    len_revwords_dic = defaultdict(list)  # {길이: [뒤집은 단어들]}

    # 이분탐색을 위해 정렬
    words.sort()
    rev_words.sort()

    for word in words:
        len_words_dic[len(word)].append(word)
    for revword in rev_words:
        len_revwords_dic[len(revword)].append(revword)

    for q in queries:
        # ?가 뒤에 올 경우
        if q[-1] == "?":
            cnt = count_in_range(
                len_words_dic[len(q)], q.replace("?", "a"), q.replace("?", "z")
            )
        # ?가 앞에 올 경우
        elif q[0] == "?":
            cnt = count_in_range(
                len_revwords_dic[len(q)],
                q[::-1].replace("?", "a"),
                q[::-1].replace("?", "z"),
            )
            answer.append(cnt)

    return answer


"""
- 분류: 구현, 문자열, 이분탐색
- 시간: 1:10-1:40 (30분)
"""
