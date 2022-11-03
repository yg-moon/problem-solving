def solution(word):
    alphas = ["A", "E", "I", "O", "U", ""]
    words = set()

    # 주의: 이렇게 만들면 첫 단어는 빈 문자열
    for i in alphas:
        for j in alphas:
            for k in alphas:
                for l in alphas:
                    for m in alphas:
                        words.add(i + j + k + l + m)

    return sorted(words).index(word)


"""
- 5중 for문
"""
