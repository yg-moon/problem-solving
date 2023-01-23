# N과 M (5)
# 출처: https://wlstyql.tistory.com/62
N, M = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()  # 사전순으로 출력하기 위해 정렬
visited = [False] * N
result = []


def solve(depth, n, m):
    if depth == m:
        print(" ".join(map(str, result)))
        return
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            result.append(nums[i])  # 핵심: 출력용 배열에, 원본 배열의 i번째 원소를 넣음
            solve(depth + 1, n, m)
            result.pop()
            visited[i] = False


solve(0, N, M)

"""
- 난이도: 실버1
- 분류: 백트래킹
"""
