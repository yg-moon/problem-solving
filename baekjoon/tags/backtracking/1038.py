# 감소하는 수
N = int(input())
result = []


def dfs(path):
    if path:
        result.append(int("".join(str(x) for x in path)))

    for i in range(10):
        # 핵심: 마지막 숫자보다 작은 숫자만 추가
        if not path or i < path[-1]:
            path.append(i)
            dfs(path)
            path.pop()


dfs([])
result.sort()

if N < 1023:
    print(result[N])
else:
    print(-1)

"""
- 난이도: 골드5
- 분류: 백트래킹

핵심
- 브루트포스는 시간초과를 받는다.
- 백트래킹으로 조건을 확인해가며 결과를 생성한다.
- 개수가 충분히 적으므로 전부 생성한 이후에 정렬한다.
"""
