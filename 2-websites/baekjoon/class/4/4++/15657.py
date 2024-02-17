# N과 M (8)
N, M = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
result = []


def dfs(start):
    if len(result) == M:
        print(*result)
        return

    for i in range(start, N):
        result.append(arr[i])
        dfs(i)
        result.pop()


dfs(0)

"""
- 난이도: 실버3
- 분류: 백트래킹

조건
- 주어진 배열에서 고를것
- N개의 자연수는 모두 다른 수
- 수열의 원소는 중복 가능
- 각 수열은 비내림차순
"""
