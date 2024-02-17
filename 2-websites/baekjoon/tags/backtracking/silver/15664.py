# N과 M (10)
N, M = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()
result = []


def dfs(path, start):
    if len(path) == M:
        result.append(path[:])  # 주의: 복사본 붙이기
        return

    # 핵심: 최근 숫자를 기억하기
    last = 0

    for i in range(start, len(nums)):
        if last != nums[i]:
            last = nums[i]
            path.append(nums[i])
            dfs(path, i + 1)
            path.pop()


dfs([], 0)

for row in result:
    print(*row)

"""
- 난이도: 실버2
- 분류: 백트래킹

- 문제: 중복이 허용된 입력에서, 중복이 없는 결과물 구하기
    - 단, 결과물에서 거르는 것은 비효율적. 만드는 과정에서 걸러야 함.
- 해결: last를 이용해서 확인
    - 이번 depth에서만 유효하고, 재귀시 초기화됨
    - visited는 필요하지 않음
"""
