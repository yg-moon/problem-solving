# 실패. (브루트포스라서 시간초과)
N, M = map(int, input().split())
balls = list(map(int, input().split()))

balls.sort()

cnt = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        if balls[i] != balls[j]:
            cnt += 1

print(cnt)
