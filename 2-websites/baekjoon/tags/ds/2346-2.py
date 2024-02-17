N = int(input())
arr = list(map(int, input().split()))

popped = [False] * N
result = []
cur = 0

for i in range(N):
    popped[cur] = True
    result.append(cur + 1)
    val = arr[cur]

    mul = 1 if val > 0 else -1
    abs_val = abs(val)

    if i == N - 1:
        break

    while abs_val > 0:
        cur = (cur + 1 * mul) % N
        if not popped[cur]:
            abs_val -= 1

print(*result)

"""
- 단순 구현 풀이도 가능
"""
