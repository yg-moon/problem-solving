# N과 M (4)
N, M = map(int, input().split())
arr = []


def dfs(start):
    if len(arr) == M:
        print(*arr)
        return

    for i in range(start, N + 1):
        arr.append(i)
        dfs(i)  # 주의: i+1이 아니라 i임 (중복허용 & 비내림차순이므로)
        arr.pop()


dfs(1)

"""
- 난이도: 실버3
- 분류: 백트래킹

조건
- N개의 자연수는 모두 다른 수
- 수열의 원소는 중복 가능
- 각 수열은 비내림차순
"""
