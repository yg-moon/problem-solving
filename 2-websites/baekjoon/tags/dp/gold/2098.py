# 외판원 순회
N = int(input())
mat = [list(map(int, input().split())) for _ in range(N)]

INF = int(1e9)

# dp[i][j]: 현재 도시가 i이고 방문현황이 j일때, 남은 도시들을 모두 거쳐 시작점으로 가는 최소비용
dp = [[-1] * (1 << N) for _ in range(N)]


def dfs(cur, visited):
    # Top-down: 이미 계산되어 있다면 그대로 리턴
    if dp[cur][visited] != -1:
        return dp[cur][visited]

    # 모든 도시를 방문했다면
    if visited == (1 << N) - 1:
        # 출발점으로 가는 경로가 있을 때
        if mat[cur][0] != 0:
            return mat[cur][0]
        # 출발점으로 가는 경로가 없을 때
        else:
            return INF

    # 다른 도시를 탐방
    min_cost = INF
    for nxt in range(1, N):
        # 가는 경로가 없다면 skip
        if mat[cur][nxt] == 0:
            continue
        # 이미 방문한 도시라면 skip
        if visited & (1 << nxt) != 0:
            continue
        # 비용 계산
        cost = dfs(nxt, visited | (1 << nxt)) + mat[cur][nxt]
        min_cost = min(min_cost, cost)

    dp[cur][visited] = min_cost

    return dp[cur][visited]


# 0번 도시를 시작점으로 잡고 출발
print(dfs(0, 1))

"""
- 난이도: 골드1
- 분류: dp

- 요약: 비트마스크 dp 유형 (탑다운 풀이)
- 참고: https://hongcoding.tistory.com/83
- 참고2: https://www.acmicpc.net/board/view/119776

핵심: 방문한 도시를 비트마스킹으로 표현하는 것
- 기본 표현: 0b'0011 <=> 0번, 1번 도시를 방문했다는 뜻
- 방문여부 확인: &를 해서, 0이 아니라면 방문했던 것
- 방문여부 추가: |를 해서, 기존 비트마스크에 추가
- 모든 도시 방문여부: (1 << N) - 1 <=> 0b'01111..
"""
