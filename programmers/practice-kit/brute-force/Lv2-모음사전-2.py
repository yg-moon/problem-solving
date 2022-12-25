def solution(word):
    alphas = ["A", "E", "I", "O", "U"]
    words_list = []

    def dfs(cnt, w):
        if cnt == 5:
            return
        for i in range(len(alphas)):
            words_list.append(w + alphas[i])
            dfs(cnt + 1, w + alphas[i])

    dfs(0, "")
    return words_list.index(word) + 1


"""
- DFS 완전탐색
"""
