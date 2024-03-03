N, K = map(int, input().split())
bags = [list(map(int, input().split())) for _ in range(N)]

answer = 0


def dfs(i, sum_w, sum_v):  # 현재까지의 (깊이, 무게, 가치)
    global answer

    # 모든 물건을 봤으면 종료
    if i == N:
        answer = max(answer, sum_v)
        return

    w = bags[i][0]
    v = bags[i][1]

    # 1. 새로운 물건을 넣지 않는 경우
    if sum_w <= K:
        dfs(i + 1, sum_w, sum_v)

    # 2. 새로운 물건을 넣는 경우
    if sum_w + w <= K:
        dfs(i + 1, sum_w + w, sum_v + v)


dfs(0, 0, 0)

print(answer)

"""
- 백트래킹 풀이 (시간초과)
"""
