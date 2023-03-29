N, K = map(int, input().split())
bags = []
for _ in range(N):
    W, V = map(int, input().split())
    bags.append((W, V))
max_val = 0


def dfs(n, w, val):
    global max_val
    # 모든 물건을 살폈다면 종료
    if n == N:
        max_val = max(max_val, val)
        return

    # 새로운 물건을 넣는 경우
    if w + bags[n][0] <= K:
        dfs(n + 1, w + bags[n][0], val + bags[n][1])

    # 이전 배낭을 들고가는 경우
    if w <= K:
        dfs(n + 1, w, val)


dfs(0, 0, 0)
print(max_val)

"""
- 참고: 백트래킹 풀이
"""
