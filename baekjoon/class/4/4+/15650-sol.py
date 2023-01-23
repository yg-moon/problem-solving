# N과 M (2)
# 출처: https://jiwon-coding.tistory.com/22
N, M = list(map(int, input().split()))
arr = []


def dfs(start):
    if len(arr) == M:
        print(" ".join(map(str, arr)))
        return

    for i in range(start, N + 1):
        if i not in arr:
            arr.append(i)
            dfs(i + 1)
            arr.pop()


dfs(1)

"""
- 난이도: 실버1
- 분류: 백트래킹
"""
