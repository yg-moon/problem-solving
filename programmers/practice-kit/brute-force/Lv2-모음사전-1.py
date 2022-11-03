from itertools import product


def solution(word):
    alphas = ["A", "E", "I", "O", "U"]
    words_list = []

    for i in range(1, 6):
        for p in list(product(alphas, repeat=i)):
            words_list.append("".join(p))

    words_list.sort()
    return words_list.index(word) + 1


"""
- 중복 순열: product
"""
