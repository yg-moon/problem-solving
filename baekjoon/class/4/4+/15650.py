# N과 M (2)
N, M = list(map(int, input().split()))
arr = []


def dfs(start):
    if len(arr) == M:
        print(*arr)
        return

    for i in range(start, N + 1):
        arr.append(i)
        dfs(i + 1)  # 오름차순이므로 다음 재귀는 i+1부터 시작
        arr.pop()


dfs(1)

"""
- 난이도: 실버1
- 분류: 백트래킹

조건
- N개의 자연수는 모두 다른 수
- 수열의 원소는 중복 불가능
- 각 수열은 오름차순
"""
