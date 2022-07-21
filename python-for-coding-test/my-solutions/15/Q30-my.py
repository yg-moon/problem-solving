# 실패.
# 정확성: ? 가 앞에 있는 경우의 처리가 잘못됨.
# 효율성: 이진탐색이 아닌 선형탐색이 들어가서 비효율적.
from bisect import bisect_left


def solution(words, queries):
    N = len(words)
    words.sort()
    words_by_len = sorted(words, key=len)
    answer = []

    def find_by_len(target):
        left = 0
        right = N - 1
        while left <= right:
            mid = (left + right) // 2
            if len(words_by_len[mid]) < target:
                left = mid + 1
            elif len(words_by_len[mid]) > target:
                right = mid - 1
            else:
                return mid
        return -1

    for query in queries:
        cnt = 0
        # ? 가 앞에 있는 경우
        if query[0] == "?":
            word = query.replace("?", "")  # ?를 제거한 접미어
            idx = find_by_len(len(query))  # 단어 길이가 일치하는 인덱스
            # 인덱스 가능한 왼쪽으로 당겨주기
            while len(words_by_len[idx]) == len(query):
                idx -= 1
            idx += 1
            # 일치하는지 검사
            while idx < N and len(words_by_len[idx]) == len(query):
                if word == "":
                    cnt += 1
                else:
                    if words_by_len[idx][len(query) - len(word) :] == word:
                        cnt += 1
                idx += 1
        # ? 가 뒤에 있는 경우
        else:
            word = query.replace("?", "")  # ?를 제거한 접두어
            idx = bisect_left(words, word)  # 해당 접두어가 처음 등장하는 인덱스
            # 접두어 패턴이 배열에 존재하면
            if idx != N:
                # 접두어 일치
                while words[idx][: len(word)] == word:
                    # 단어 길이 일치
                    if len(words[idx]) == len(query):
                        cnt += 1
                    idx += 1
        answer.append(cnt)

    return answer
