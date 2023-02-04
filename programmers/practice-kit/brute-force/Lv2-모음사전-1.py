from itertools import product


def solution(word):
    alphas = ["A", "E", "I", "O", "U"]
    words = []

    for i in range(1, 6):
        for p in list(product(alphas, repeat=i)):
            words.append("".join(p))

    words.sort()

    return words.index(word) + 1


"""
- 중복 순열: itertools.product
"""
