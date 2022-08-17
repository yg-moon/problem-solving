n, k = map(int, input().split())

cnt = 0
while n >= k:
    # 나누어 떨어질 때 까지 빼기
    target = (n // k) * k
    cnt += n - target
    n = target

    # 나누기
    n //= k
    cnt += 1

# 남은 수가 1이 될 때 까지 빼기
cnt += n - 1

print(cnt)
