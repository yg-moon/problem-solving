N, K = map(int, input().split())

cnt = 0
while N >= K:
    # 나누어 떨어질 때 까지 빼기
    target = (N // K) * K
    cnt += N - target
    N = target

    # 나누기
    N //= K
    cnt += 1

# 남은 수가 1이 될 때 까지 빼기
cnt += N - 1

print(cnt)
