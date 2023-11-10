# 감소하는 수
def dfs(path):
    if path:
        result.append(int("".join(str(x) for x in path)))

    for i in range(10):
        # 마지막 숫자보다 작은 숫자만 추가
        if not path or i < path[-1]:
            path.append(i)
            dfs(path)
            path.pop()


N = int(input())
result = []
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
- 정말 무식한 방법은 시간초과를 받는다.
- 조건을 만족하는지 매번 확인해가며 결과를 생성한다.
- 개수가 적으므로 전부 생성한 이후에 정렬한다.
"""
