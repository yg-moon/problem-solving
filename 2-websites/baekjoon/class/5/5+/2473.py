# 세 용액
N = int(input())
arr = list(map(int, input().split()))

arr.sort()

min_diff = int(1e13)  # 주의: 1e9로 하면 안됨
answer = []

for i in range(N - 2):
    l = i + 1
    r = N - 1

    while l < r:
        cur_sum = arr[i] + arr[l] + arr[r]

        if abs(cur_sum) < min_diff:
            min_diff = abs(cur_sum)
            answer = [arr[i], arr[l], arr[r]]

        if cur_sum < 0:
            l += 1
        else:
            r -= 1

print(*answer)

"""
- 난이도: 골드3
- 분류: 투포인터

- 핵심: 하나를 고정하고, 나머지를 이분탐색
"""
