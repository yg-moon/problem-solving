# N과 M (9)
N, M = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
visited = [False] * N
result = []


def dfs():
    if len(result) == M:
        print(*result)
        return

    prev = 0  # 핵심: 중복수열 방지

    for i in range(N):
        if not visited[i] and prev != arr[i]:
            visited[i] = True
            result.append(arr[i])
            prev = arr[i]
            dfs()
            result.pop()
            visited[i] = False


dfs()

"""
- 난이도: 실버2
- 분류: 백트래킹

조건
- 주어진 배열에서 고를것
- N개의 자연수는 모두 다른 수가 아님
    - 이미 출력한 수열은 다시 출력하면 안 됨
- 수열의 원소는 중복 불가능
- 전체 결과는 사전순으로 증가하는 순서로 출력
"""
