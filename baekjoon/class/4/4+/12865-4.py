# 평범한 배낭
# 출처: https://ji-gwang.tistory.com/m/435
N, K = map(int, input().split())
bags = [tuple(map(int, input().split())) for _ in range(N)]  # 주의: 이번 경우 1-idx가 아님

# dp[i][j]: 이번 경우 개별 칸은 별 의미없고, dp[0][0]에 최종정답이 저장됨
# (굳이 표현하자면 i번째 물건부터 사용해서, 여유무게 j가 남도록 구성 가능한 최대가치)
dp = [[-1] * (K + 1) for _ in range(N + 1)]


def dfs(n, w):
    # 무게 초과
    if w > K:
        return -int(1e9)

    # 개수 초과
    if n == N:
        return 0

    # 이미 계산한 경우라면 그대로 리턴
    if dp[n][w] != -1:
        return dp[n][w]

    # 점화식: max(이전 배낭 그대로 들고가기, 현재 물건 넣기)
    dp[n][w] = max(dfs(n + 1, w), dfs(n + 1, w + bags[n][0]) + bags[n][1])
    return dp[n][w]


print(dfs(0, 0))

"""
- (0,0)에서 시작하는 Top-down 냅색

참고
- 냅색 문제의 경우 바텀업이 가장 잘 어울리고, (0,0)에서 시작하는 탑다운이 제일 안 어울린다.
- 일단 dp 배열의 정의만 봐도 뭔가 어색한 것을 느낄 수 있다. 문제와 어울리지 않는 풀이법이다.
- 하지만 다른 문제의 경우 (0,0)부터 시작하는게 자연스러운 경우도 많다.
"""
