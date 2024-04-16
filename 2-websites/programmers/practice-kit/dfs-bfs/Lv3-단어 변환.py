# 한글자만 바꿔서 변환 가능한지 체크: 두 문자열에서 다른 문자가 정확히 1개인 경우
def is_changeable(word_1, word_2):
    diff = 0
    for i in range(len(word_1)):
        if word_1[i] != word_2[i]:
            diff += 1
    return diff == 1


def solution(begin, target, words):
    # 예외처리를 통한 최적화: target이 words안에 없을 경우 (원천적으로 불가능)
    if target not in words:
        return 0

    answer = int(1e9)
    visited = set()

    def dfs(cur, step):
        if cur == target:
            nonlocal answer
            answer = min(answer, step)
        for word in words:
            if word not in visited and is_changeable(cur, word):
                visited.add(word)
                dfs(word, step + 1)
                visited.remove(word)

    dfs(begin, 0)

    # 어떠한 방법으로도 변환할 수 없는지 체크: 초기값 그대로일 경우
    if answer == int(1e9):
        return 0
    else:
        return answer


"""
- 백트래킹
"""
