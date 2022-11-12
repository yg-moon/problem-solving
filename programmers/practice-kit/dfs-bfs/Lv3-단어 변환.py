def changeable(word_1, word_2):
    diff_cnt = 0

    for i in range(len(word_1)):
        if word_1[i] != word_2[i]:
            diff_cnt += 1
        if diff_cnt == 2:
            return False

    if diff_cnt == 1:
        return True
    else:
        return False


def solution(begin, target, words):
    # 예외케이스 최적화
    if target not in words:
        return 0

    min_steps = int(1e9)
    visited = set()

    def dfs(curr, step):
        if curr == target:
            nonlocal min_steps
            min_steps = min(min_steps, step)

        for word in words:
            if word not in visited and changeable(curr, word):
                visited.add(word)
                dfs(word, step + 1)
                visited.remove(word)

    dfs(begin, 0)

    if min_steps == int(1e9):
        return 0
    else:
        return min_steps


"""
- 요약: DFS 완전탐색
- 구현
    - 한글자만 바꿔서 변환 가능한지 체크 → 두 문자열에서 다른 문자가 정확히 1개인 경우
    - 어떠한 방법으로도 변환할 수 없는지 체크 → `min_steps` 가 초깃값 그대로일 경우
    - 예외처리를 통한 추가 최적화 → `target`이 `words`안에 없을 경우 (원천적으로 불가능)
"""
