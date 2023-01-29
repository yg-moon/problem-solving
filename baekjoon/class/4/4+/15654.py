# N과 M (5)
# 출처: https://wlstyql.tistory.com/62
N, M = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()  # 사전순으로 출력하기 위해 정렬
visited = [False] * N  # 주어진 배열에 대해 작업하는데, 원소는 중복 불가능이므로 방문여부를 확인
result = []


def dfs():
    if len(result) == M:
        print(*result)
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            result.append(arr[i])  # 핵심: 출력용 배열에, 원본 배열의 i번째 원소를 넣음
            dfs()
            result.pop()
            visited[i] = False


dfs()

"""
- 난이도: 실버1
- 분류: 백트래킹

조건
- 주어진 배열에서 고를것
- N개의 자연수는 모두 다른 수
- 수열의 원소는 중복 불가능
- 전체 결과는 사전순으로 증가하는 순서로 출력
"""
