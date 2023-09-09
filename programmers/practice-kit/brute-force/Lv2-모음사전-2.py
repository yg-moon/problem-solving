def solution(word):
    alphas = ["A", "E", "I", "O", "U"]
    words = []

    def dfs(cnt, w):
        if cnt == 5:
            return
        for i in range(len(alphas)):
            words.append(w + alphas[i])
            dfs(cnt + 1, w + alphas[i])

    dfs(0, "")

    return words.index(word) + 1


"""
- 백트래킹 (정해)
"""
