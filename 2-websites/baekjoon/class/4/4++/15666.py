# N과 M (12)
N, M = map(int, input().split())
arr = list(set((map(int, input().split()))))  # 핵심: 중복 원소를 제거하고 받음

arr.sort()
result = []


def dfs(start):
    if len(result) == M:
        print(*result)
        return

    for i in range(start, len(arr)):
        result.append(arr[i])
        dfs(i)
        result.pop()


dfs(0)

"""
- 난이도: 실버2
- 분류: 백트래킹

조건
- 주어진 배열에서 고를것
- N개의 자연수는 모두 다른 수가 아님
    - 이미 출력한 수열은 다시 출력하면 안 됨
- 수열의 원소는 중복 가능
- 각 수열은 비내림차순
- 전체 결과는 사전순으로 증가하는 순서로 출력
"""
