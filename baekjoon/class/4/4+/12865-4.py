N, K = map(int, input().split())
bags = [tuple(map(int, input().split())) for _ in range(N)]

# dp[i][j]: 개별 칸은 별 의미없고, dp[0][0]에 최종정답이 저장됨
# (굳이 표현하자면 i번째 물건부터 사용해서, 여유무게 j가 남도록 구성 가능한 최대가치)
dp = [[-1] * (K + 1) for _ in range(N + 1)]


def dfs(i, j):
    # base case 1: 무게 초과
    if j > K:
        return -int(1e9)

    # base case 2: 개수 초과 (주의: base case 확인 순서가 바뀌면 안됨)
    if i == N:
        return 0

    # top-down
    if dp[i][j] != -1:
        return dp[i][j]

    w = bags[i][0]
    v = bags[i][1]

    # 점화식: max(새로 안 넣기, 새로 넣기)
    dp[i][j] = max(dfs(i + 1, j), dfs(i + 1, j + w) + v)

    return dp[i][j]


print(dfs(0, 0))

"""
- (0,0)에서 시작하는 Top-down DP (1296ms)
- dp 배열 정의부터 보이듯이 가장 부자연스러운 풀이법
- 참고: https://ji-gwang.tistory.com/m/435
"""
