# N과 M (10)
N, M = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()
visited = [False] * N
result = []


def dfs(path, start):
    if len(path) == M:
        result.append(path[:])
        return

    # 핵심: 마지막 숫자를 기억
    last = 0

    for i in range(start, len(nums)):
        if not visited[i] and last != nums[i]:
            visited[i] = True
            path.append(nums[i])
            last = nums[i]
            dfs(path, i + 1)
            path.pop()
            visited[i] = False


dfs([], 0)

for row in result:
    print(*row)

"""
- 난이도: 실버2
- 분류: 백트래킹

- 문제: 중복이 허용된 입력에서, 중복을 허용하지 않은 결과물 구하기 (결과물에서 중복을 거르는 것은 비효율적)
- 해결: visited 정보와 last 변수를 이용해서 확인 (정렬을 했으므로 항상 성립)
"""
